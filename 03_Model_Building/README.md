:calendar: 
## Day 4 Part 1:

Welcome to the Mode Training section of the ML Workshop. This section is divided into 2 parts
-  Model Training on AWS SageMaker
-  Model Evaluation Pipeline using AWS Glue and QuickSights

## Pre-Requisites:
1.	You should have created an AWS account and verified some of the key access to key resources we will be using in this 4 day’s workshop
2.	You have created an IAM role that you will be using in this series, with the necessary permissions
3.	You have created an S3 bucket and can access the git repo shared earlier.

## Key Objectives:
By the end of this section, you should have a good idea on 
1.	How to build Machine Learning/Deep Learning models , using AWS SageMaker on the data which was prepped in Day 2 
2. How to build a pipeline using AWS Glue to store the model results to Athena databzse and use QuickSights dashboards to view them 

## Post-Requisites:
- Delete QuickSights Account
- Delete roles pertaining to QuickSights
- ![Screen Shot 2022-04-04 at 10 27 56 PM](https://user-images.githubusercontent.com/9430155/161685014-1f43bd18-7a2d-450c-aed3-4b2093a963c2.png)
- ![Screen Shot 2022-04-04 at 10 28 07 PM](https://user-images.githubusercontent.com/9430155/161685022-4c208418-3abd-44eb-917a-2ba6801a26fe.png)
- ![Screen Shot 2022-04-04 at 10 28 15 PM](https://user-images.githubusercontent.com/9430155/161685030-3d848520-7912-41f5-9a9d-cf2b4cfc3014.png)

## Missed it? Dont Worry 
If you missed this session, please follow the below steps:
- Create a AWS SageMaker notebook instance by following the steps here: https://github.com/ConcurDataScience/ConcurMLWorkshop
- Download the files from here and upload it to your notebook instance
- If you have already cloned the repository, it should already be available
- There is a power point slide attached in the repo. Please use that for reference
- Delete QuickSights Account and IAM roles having QuickSights in them

## Contact
For any questions, please feel free to email me at adithya.kumar@sap.com or Slack me at @i849730
