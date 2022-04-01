:calendar:
### Day 2 Part2:

Welcome to the Data Labeling section of the ML Workshop. This morning we have gone through the process of how to aquire some already labeled data. However, in real life, you don't always get lucky to have labeled data. Very often, you will need to get your own data labeled. In this section, we will go through the process of setting up a labeling job using GroundTruth in AWS Sagemaker and preparing it for consumption by our Model.

### Pre-Requisites:
1.	You should have created an AWS account.
2.  You have checked out this github project to your local disk
3.	If you missed the prior classes, please make sure that you have followed the general instruction in the github project home to
* create the IAM role: <b>ConcurMLWorkshopUse</b>.
* create your S3 bucket.
* create and start your notebook instance (Make sure that the notebook was create in the us-west-2 region and assigned the above IAM role)

Doing these preparation is important because some of the steps such as creating the notebook instance can take upto 10 minutes.

### Key Objectives:
By the end of this section, you should have a good idea on
1.	What is a labeling UI template.
2.	How to prepare the input manifest file for your labeling job.
3.	How to create the labeling job.
4.  How to prepare the labeling output for consumption by your model.

### Steps We will go through:
1.	(HO) Before we start, we need to create the notebook instance first in SageMaker.
2.	(HO) We will learn how to prepare the data needed for creating a labeling job in AWS.
3.	(HO) We will learn how to create a new labeling job in AWS console and how to automate it with code.
4.	(HO) We will learn how to process the labeling output for consumption by a model
7.	(P) Finally, we will show what is possible with a quick demo of our labeling pipeline and our custome Bounding-box NER liquid template.

* HO-Hands On
* P-Presentation Slides

### Post-Requisites:
After the session’s completion, you should have some data labeled and ready to be used for Model Training.


### Missed it ? Dont Worry
Because Part1 already prepared some labeled data, you should be fine to continue to the next part even if you missed this session.

### Cleanup Instruction:
The following resource are created after this session. Please follow the cleanup instructions to avoid incur any unnecessary charges.

1. Athena database with tables: <b>ml-workshop-db</b>. You can delete at the end of the week. To delete, run "drop database `ml-workshop-db`" in Athena Query Editor.
2. S3 bucket: You can go to the S3 console and delete it at the end of the week.
3. GroundTruth jobs: AWS does not have a mechanism to delete the jobs. Failed or completed jobs will not incur any changes. If you have finished the exercises, the job should be in the completed status. In case if you did not finish the exercise, you can stop the job to avoid incur any charge after that.
4. SageMaker notebook instance:
* You can stop the instance at the end of each day.
* Start the notebook before the first session of the day.
* Delete the notebook instance when the class is finished.
5. Cognito User Pool (created by Amazon automatically): <b>sagemaker-groundtruth-user-pool</b>. For free tier, if you have less than 50000 MAUs, it is free and so we recommand that you do not delete this. If you do delete it, it will stop you from being able to create new labeling job again. You can check for the pricing [here](https://aws.amazon.com/cognito/pricing/) for more detail.

<strong>Disclaimer, the instruction here does not supersede the AWS pricing policy. When in doubt about what cost it might incur, please check the corresponding pricing page from Amazon.</strong>