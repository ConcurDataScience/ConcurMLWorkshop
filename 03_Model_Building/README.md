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

- Glue Crawler to save model results to Athena
- ![Screen Shot 2022-04-04 at 11 10 07 PM](https://user-images.githubusercontent.com/9430155/161690230-8295dcd7-a1d6-4ea9-a2a8-08640006a3a3.png)
- ![Screen Shot 2022-04-04 at 11 10 13 PM](https://user-images.githubusercontent.com/9430155/161690234-cd020afe-9e68-43fd-8bc0-d9e46568ae26.png)
- ![Screen Shot 2022-04-04 at 11 10 34 PM](https://user-images.githubusercontent.com/9430155/161690300-2fe6f77b-6e28-4382-bab2-99ae1984bdef.png)
- ![Screen Shot 2022-04-04 at 11 10 41 PM](https://user-images.githubusercontent.com/9430155/161690314-31230ac2-e0b3-47ba-a84c-a71b4eb1b502.png)
- ![Screen Shot 2022-04-04 at 11 10 50 PM](https://user-images.githubusercontent.com/9430155/161690332-f5519010-14fe-4ad2-b58c-02e8e71cb60f.png)
- ![Screen Shot 2022-04-04 at 11 10 55 PM](https://user-images.githubusercontent.com/9430155/161690345-12f02d28-0796-499f-b594-c9909a6cdc62.png)
- ![Screen Shot 2022-04-04 at 11 11 09 PM](https://user-images.githubusercontent.com/9430155/161690360-c056e299-1d78-4241-a0b7-6b1dae3b2673.png)
- ![Screen Shot 2022-04-04 at 11 11 16 PM](https://user-images.githubusercontent.com/9430155/161690376-abf6ae9b-a100-42ba-aa19-f2a90cc0935f.png)




- 



## Missed it? Dont Worry 
If you missed this session, please follow the below steps:
- Create a AWS SageMaker notebook instance by following the steps here: https://github.com/ConcurDataScience/ConcurMLWorkshop
- Download the files from here and upload it to your notebook instance
- If you have already cloned the repository, it should already be available
- There is a power point slide attached in the repo. Please use that for reference
- Delete QuickSights Account and IAM roles having QuickSights in them

## Contact
For any questions, please feel free to email me at adithya.kumar@sap.com or Slack me at @i849730
