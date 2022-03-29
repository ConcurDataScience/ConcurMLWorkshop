:calendar: 
### Day 2 Part2:

Welcome to the Data Labeling section of the ML Workshop. This morning we have gone through ptocess of how to aquire some already labeled data. However, in real life, you don't always get lucky to have already labeled data. Most of the time, you need to label your data. In this section, we will go through the process of setting up a labeling job using AWS Sagemaker and preparing it for consumption by our Model.

### Pre-Requisites:
1.	You should have created an AWS account and verified some of the key access to key resources we will be using in this 4 day’s workshop
2.	You have created an IAM role that you will be using in this series, with the necessary permissions
3.	You have created an S3 bucket and can access the git repo shared earlier.
4.	You have downloaded the data into that S3 bucket.

### Key Objectives:
By the end of this section, you should have a good idea on
1.	How to work with a labeling UI template.
2.	How to prepare the input manifest file for your labeling job.
3.	How to create the labeling job.
4.  How to do ETL on the labeling output and make it easily consumable by your model

### Steps We will go through:
1.	(HO) Before we dive deep into the code, I will first demo using the AWS Groundtruth console to create a new job
2.	(HO) We will learn the concept of labeling UI template and upload a template to S3
3.	(HO) We will learn the concept of the input manifest and upload the input manifest to S3
4.	(HO) We will create a new job
5.	(HO) We will do the labels.
6.	(P) We will review the label outputs
7.  (HO) We will do ETL on the labeling output
7.	(P) Finally, we review the Athena table produced by the ETL.

*HO-Hands On
*P-Presentation Slides

### Post-Requisites:
•	After the session’s completion, you should have some data labeled and ready to be used for Model Training.


### Missed it ? Dont Worry
Because Part1 already prepared some labeled data, you should be fine to continue to the next part even if you missed this session.

