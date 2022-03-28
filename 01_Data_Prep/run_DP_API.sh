sudo su
echo "Running DP API!"
echo "Getting todays available data from DP API!"
aws s3 cp s3://datascience-ml-workshop-prep/data_prep_component/DP_staging/upserts/ s3://datascience-ml-workshop-prep/data_prep_component/upserts/ --recursive
aws s3 cp s3://datascience-ml-workshop-prep/data_prep_component/DP_staging/deletes/ s3://datascience-ml-workshop-prep/data_prep_component/deletes/  --recursive
echo "Processing Finised!"