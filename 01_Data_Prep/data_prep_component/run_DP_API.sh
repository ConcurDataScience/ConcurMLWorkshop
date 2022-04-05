#!/usr/bin/env bash

usage="Usage: bash run_DP_API.sh {bucket_name}"

if [ -z "$1" ]; then
  echo "$usage"
  exit 101
fi
bucket_name=$1
echo "Running DP API!"
echo "Getting todays available data from DP API!"
aws s3 cp s3://${bucket_name}/data_prep_component/DP_staging/upserts/ s3://${bucket_name}/data_prep_component/upserts/ --recursive
aws s3 cp s3://${bucket_name}/data_prep_component/DP_staging/deletes/ s3://${bucket_name}/data_prep_component/deletes/ --recursive
echo "Processing Finised!"