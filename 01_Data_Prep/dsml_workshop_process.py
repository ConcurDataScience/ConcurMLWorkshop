import boto3
import botocore
import sys
from pyspark.sql import functions as F
from pyspark.sql import types as T
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql import SparkSession
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.utils import getResolvedOptions
from awsglue.job import Job

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = SparkSession.builder.appName("index_create").getOrCreate()
job = Job(glueContext)
spark.conf.set("spark.sql.sources.partitionOverwriteMode","DYNAMIC")
s3_client = boto3.client('s3')


def load_latest(spark, bucket_name, source, upsert_or_delete):
    prefix = str(source + '/' + upsert_or_delete+ '/')
    path = get_most_recent_s3_object(bucket_name, prefix)
    print("Currently Reading", path)
    df = spark.read.csv(path, header=True, sep='\t')
    df = df.drop('_c0')
    return df

def get_most_recent_s3_object(bucket_name,prefix):
    s3 = boto3.client('s3')
    paginator = s3.get_paginator( "list_objects_v2" )
    page_iterator = paginator.paginate(Bucket=bucket_name, Prefix=prefix)
    latest = []
    for page in page_iterator:
        if "Contents" in page:
            latest.append(max(page['Contents'], key=lambda x: x['LastModified']))
    total_max = max(latest, key=lambda x: x['LastModified'])
    latest_data_path = total_max['Key']
    latest_data_path = "/".join(latest_data_path.split("/")[:-1])
    return str('s3://'+ bucket_name + '/' + latest_data_path)  

def process_incrememtal_upserts(spark,delta_upserts, processed_data):
    df = processed_data.unionByName(delta_upserts)
    w = Window.partitionBy('dp_unique_key').orderBy(F.desc('updated_date'))
    df = df.withColumn('Rank',F.dense_rank().over(w))
    final_upsert_data = df.filter(df.Rank == 1).drop(df.Rank)
    return final_upsert_data

def process_first_upserts(spark,delta_upserts): 
    return delta_upserts
    

def process_incrememtal_deletes(spark, delta_deletes, processed_data):
    if delta_deletes.count()>0:
        data_post_delete_processing = processed_data.join(delta_deletes, 'dp_unique_key','left_anti')
        return data_post_delete_processing
    else:
        return None
    
def write_files(data, bucket_name, destination, script_type='processed_data'):
    data.write.mode("overwrite").csv("s3://" + bucket_name+ "/" + destination + "/tmp/" + script_type + "_tmp", header=True, sep='\t')
    data =spark.read.csv("s3://"+bucket_name + "/"+ destination +"/tmp/"+ script_type + "_tmp", header=True, sep='\t')
    data.write.mode("overwrite").csv("s3://" + bucket_name + "/" + destination +"/"+ script_type, header=True, sep='\t')
    
    
bucket_name = 'datascience-ml-workshop-prep'
source = 'data_prep_component'
destination = 'labeling_data_component/data_prep_output'
run = "incremental"


bucket_name = 'datascience-ml-workshop-prep'
source = 'data_prep_component'
destination = 'labeling_data_component/data_prep_output'
run = "incremental"
try:
    processed_data = spark.read.csv("s3://"+bucket_name+ "/"+destination+"/processed_data/", header=True, sep='\t')
except:
    run="first"
delta_upserts = load_latest(spark, bucket_name, source,  'upserts')
if run=="first":
    print("processing_first_run")
    final_data = process_first_upserts(spark, delta_upserts)
else:
    print("processing_incremental_run")
    final_data = process_incrememtal_upserts(spark,delta_upserts,processed_data)
    
print("Count of 2nd batch upserts:", delta_upserts.count())
print("Count After 2nd batch upserts is processed:", final_data.count())
write_files(final_data, bucket_name, destination)


delta_deletes = load_latest(spark, bucket_name, source,  'deletes')
processed_data = spark.read.csv("s3://"+bucket_name+ "/"+destination+"/processed_data", header=True, sep='\t')
data_post_delete_processing = process_incrememtal_deletes(spark, delta_deletes, processed_data)
if data_post_delete_processing is not None:
    write_files(data_post_delete_processing, bucket_name, destination)
processed_data = spark.read.csv("s3://"+bucket_name+ "/"+destination+"/processed_data", header=True, sep='\t')
print("Count of 2nd batch Delete:", delta_deletes.count())
print("Count After 2nd batch upserts & Deletes are processed:", processed_data.count())