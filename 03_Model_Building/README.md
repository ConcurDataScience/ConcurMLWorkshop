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
- ![Screen Shot 2022-04-04 at 11 20 56 PM](https://user-images.githubusercontent.com/9430155/161691386-208fe0e9-53c4-41a2-a000-0333084e8e92.png)

## Missed it? Dont Worry 
If you missed this session, please follow the below steps:
- Create a AWS SageMaker notebook instance by following the steps here: https://github.com/ConcurDataScience/ConcurMLWorkshop
- Download the files from here and upload it to your notebook instance
- If you have already cloned the repository, it should already be available
- Run all the cells in the Jupyter lab notebook (Make sure you have selected the conda_tensorflow_p36 kernel type on the top right corner of your Jupyterlab) 
- There is a power point slide attached in the repo too. Please use that for reference/theoretical concepts
- Run Glue Crawler to save model results in S3 to Athena

- ![Screen Shot 2022-04-04 at 11 10 07 PM](https://user-images.githubusercontent.com/9430155/161690230-8295dcd7-a1d6-4ea9-a2a8-08640006a3a3.png)
- ![Screen Shot 2022-04-04 at 11 10 13 PM](https://user-images.githubusercontent.com/9430155/161690234-cd020afe-9e68-43fd-8bc0-d9e46568ae26.png)
- ![Screen Shot 2022-04-04 at 11 10 34 PM](https://user-images.githubusercontent.com/9430155/161690300-2fe6f77b-6e28-4382-bab2-99ae1984bdef.png)
- ![Screen Shot 2022-04-04 at 11 10 41 PM](https://user-images.githubusercontent.com/9430155/161690314-31230ac2-e0b3-47ba-a84c-a71b4eb1b502.png)
- ![Screen Shot 2022-04-04 at 11 10 50 PM](https://user-images.githubusercontent.com/9430155/161690332-f5519010-14fe-4ad2-b58c-02e8e71cb60f.png)
- ![Screen Shot 2022-04-04 at 11 10 55 PM](https://user-images.githubusercontent.com/9430155/161690345-12f02d28-0796-499f-b594-c9909a6cdc62.png)
- ![Screen Shot 2022-04-04 at 11 11 09 PM](https://user-images.githubusercontent.com/9430155/161690360-c056e299-1d78-4241-a0b7-6b1dae3b2673.png)
- ![Screen Shot 2022-04-04 at 11 11 16 PM](https://user-images.githubusercontent.com/9430155/161690376-abf6ae9b-a100-42ba-aa19-f2a90cc0935f.png)
- ![Screen Shot 2022-04-04 at 11 14 11 PM](https://user-images.githubusercontent.com/9430155/161691111-f53ee14b-9d25-4f17-995f-114a3b149193.png)

- Create QuickSights dashboards to view model results
- Click Manage QuickSights on the top right corner 
- Navigate to Security and Permissions
- Click Manage under - QuickSight access to AWS services
- Select S3 buckets and choose the bucket you had created earlier
- Save your changes
- ![Screen Shot 2022-04-04 at 11 43 46 PM](https://user-images.githubusercontent.com/9430155/161695250-38b4bf00-368a-4099-91b8-72ae0203847d.png)
- ![Screen Shot 2022-04-04 at 11 43 38 PM](https://user-images.githubusercontent.com/9430155/161695253-83b21c95-164a-404c-8d9f-65e7a2e8b790.png)
- ![Screen Shot 2022-04-04 at 11 43 29 PM](https://user-images.githubusercontent.com/9430155/161695255-77ff05a9-3849-4813-98f9-b4f27981a8cf.png)

- ![Screen Shot 2022-04-04 at 11 16 31 PM](https://user-images.githubusercontent.com/9430155/161690972-49f66e47-3938-432e-8536-e2d0b65a8e62.png)
- ![Screen Shot 2022-04-04 at 11 16 53 PM](https://user-images.githubusercontent.com/9430155/161690993-6a5a227e-4e80-4d4e-92cc-557219351732.png)
- ![Screen Shot 2022-04-04 at 11 17 03 PM](https://user-images.githubusercontent.com/9430155/161691171-8b3aaf5c-3e7b-431b-bfe8-648206e94e82.png)
- ![Screen Shot 2022-04-04 at 11 17 12 PM](https://user-images.githubusercontent.com/9430155/161691187-782b7a0e-211f-405d-a7f3-cb2888809edc.png)
- ![Screen Shot 2022-04-04 at 11 17 17 PM](https://user-images.githubusercontent.com/9430155/161691209-1c3fbe08-f85d-4c39-bbe6-489000f69644.png)
- ![Screen Shot 2022-04-04 at 11 17 27 PM](https://user-images.githubusercontent.com/9430155/161691221-74d5f910-5732-4ab6-90aa-c4c80e3c5614.png)

- Delete QuickSights Account and IAM roles having QuickSights in them (Refer screenshots above)

## Contact
For any questions, please feel free to email me at adithya.kumar@sap.com or Slack me at @i849730
