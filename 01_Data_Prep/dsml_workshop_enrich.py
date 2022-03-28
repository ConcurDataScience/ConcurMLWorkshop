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

bucket_name = 'datascience-ml-workshop-prep'
source = 'data_prep_component'
destination = 'labeling_data_component/data_prep_output'
run = "incremental"

def write_files(data, bucket_name, destination, script_type='processed_data'):
    data.write.mode("overwrite").csv("s3://" + bucket_name+ "/" + destination + "/tmp/" + script_type + "_tmp", header=True, sep='\t')
    data =spark.read.csv("s3://"+bucket_name + "/"+ destination +"/tmp/"+ script_type + "_tmp", header=True, sep='\t')
    data.write.mode("overwrite").csv("s3://" + bucket_name + "/" + destination +"/"+ script_type, header=True, sep='\t')

data_part_2 = spark.read.csv('s3://'+bucket_name +'/'+ source + '/id_entity_mapper.csv',header=True )
data_part_1 = spark.read.csv("s3://"+bucket_name+ "/"+destination+"/processed_data", header=True, sep='\t')
joined_data = data_part_1.join(data_part_2, ['Id','dp_unique_key'], 'inner').drop('_c0')
print("Joined Data Count", joined_data.count())
write_files(joined_data, bucket_name, destination, 'enriched_data')