:calendar:
### Day 2 Part2:

Welcome to the Data Labeling section of the ML Workshop. This morning we have gone through the process of how to aquire some already labeled data. However, in real life, you don't always get lucky to have labeled data. Very often, you will need to get your own data labeled. In this section, we will go through the process of setting up a labeling job using GroundTruth in AWS Sagemaker and preparing it for consumption by our Model.

### Files used in this session:
| Name  |  Description |
|---|---|
| README.md | This file |
| labeling.ipynb | The code and detail instrtuctions of the class |
| resources/tweet_data.csv  | The raw source data used by the labeling job we will create in the class |
| resources/sentiments.json  | Dependency of the labeling job used in the class. The categories used by the job |
| resources/sentiment-analysis-tweet.liquid  | Dependency of the labeling job used in the class. The UI template of the job |

### <img width="20" src="https://user-images.githubusercontent.com/769011/161400643-c2242bd9-75e7-4fcd-a9e2-2c5174c67b97.png">Pre-Requisites:
1.	You should have created an AWS account.
2.  You have checked out this github project to your local disk
3.	If you missed the prior classes, please make sure that you have followed the general instruction in the github project home to
* create the IAM role: <i>ConcurMLWorkshopUse</i>. <b>Check the IAM role to make sure that you have acces to S3, Athena and SageMaker.</b>
* create your S3 bucket. <b>Verify that in the Properties tab, you see us-west-2 as the region.</b>
* create and start your notebook instance. <b>Verify that it has the role <i>ConcurMLWorkshopUse</i> and it is listed under us-west-2 region.</b>

<img width="622" alt="iamrole" src="https://user-images.githubusercontent.com/769011/161399924-dbe2b37a-39fe-438c-b35f-f090d646fecf.png">
<img width="472" alt="Screen Shot 2022-04-02 at 5 49 26 PM" src="https://user-images.githubusercontent.com/769011/161406515-6f52e30f-b462-4b93-ab0f-ffe46446d1c0.png">
<img width="200" alt="Screen Shot 2022-04-02 at 1 24 47 PM" src="https://user-images.githubusercontent.com/769011/161400029-88ae24d4-bf57-4436-bac5-28ba6e520df3.png">
<img width="800" alt="Screen Shot 2022-04-02 at 1 27 31 PM" src="https://user-images.githubusercontent.com/769011/161400105-097f31f5-4c4f-4262-b733-94f9716b8158.png">


Doing these preparation is important because some of the steps such as creating the notebook instance can take up to 10 minutes.

### Key Objectives:
By the end of this section, you should have a good idea on
1.	What is a labeling UI template.
2.	How to prepare the input manifest file for your labeling job.
3.	How to create the labeling job.
4.  How to prepare the labeling output for consumption by your model.

### Steps We will go through:
1.	(HO) We will learn how to prepare the data needed for creating a labeling job in AWS.
2.	(HO) We will learn how to create a new labeling job in AWS console and how to automate it with code.
3.	(HO) We will learn how to process the labeling output for consumption by a model
4.	(P) Finally, we will show what is possible with a quick demo of our labeling pipeline and our custome Bounding-box NER liquid template.

* HO-Hands On
* P-Presentation Slides

### Post-Requisites:
After the session’s completion, you should have some data labeled and ready to be used for Model Training.


### Missed it ? Dont Worry
Because Part1 already prepared some labeled data, you should be fine to continue to the next part even if you missed this session.

### Cleanup Instruction:
The following resources are created after this session. Please follow the cleanup instructions to avoid incur any unnecessary charges on you.

1. Athena database with tables: <b>ml-workshop-db</b>. You can delete at the end of the week. To delete, run "drop database `ml-workshop-db`" in Athena Query Editor.
2. S3 bucket: You can go to the S3 console and delete it at the end of the week.
3. GroundTruth jobs: AWS does not have a mechanism to delete the jobs. Failed or completed jobs will not incur any changes. If you have finished the exercises, the job should be in the completed status. In case if you did not finish the exercise, you can stop the job to avoid any charges after that.
4. SageMaker notebook instance:
* You can stop the instance at the end of each day.
* Start the notebook before the first session of the day. It can take up to 5 to 10 minutes to start your notebook instance.
* Delete the notebook instance when the class is finished by the end of the week.
5. Cognito User Pool (created by Amazon automatically): <b>sagemaker-groundtruth-user-pool</b>. For free tier, if you have less than 50000 MAUs, it is free and so we recommand that you do not delete this. If you do delete it, it will stop you from being able to create new labeling job again. You can check for the pricing [here](https://aws.amazon.com/cognito/pricing/) for more detail.

<strong>Disclaimer, the instruction here does not supersede the AWS pricing policy. When in doubt about what cost it might incur, please check the corresponding service pricing page from Amazon.</strong>
