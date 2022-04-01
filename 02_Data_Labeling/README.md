:calendar:
### Day 2 Part2:

Welcome to the Data Labeling section of the ML Workshop. This morning we have gone through the process of how to aquire some already labeled data. However, in real life, you don't always get lucky to have labeled data. Very often, you will need to get your own data labeled. In this section, we will go through the process of setting up a labeling job using GroundTruth in AWS Sagemaker and preparing it for consumption by our Model.

### Pre-Requisites:
1.	You should have created an AWS account and verified some of the key access to key resources we will be using in this 4 day’s workshop
2.	You have created an IAM role that you will be using in this series, with the necessary permissions
3.	You have created an S3 bucket and can access the git repo shared earlier.
4.	You have created and started your notebook instance (Make sure that the notebook was create in the us-west-2 region)

### Key Objectives:
By the end of this section, you should have a good idea on
1.	What is a labeling UI template.
2.	How to prepare the input manifest file for your labeling job.
3.	How to create the labeling job.
4.  How to prepare the labeling output for consumption by your model.

### Steps We will go through:
1.	(HO) Before we start, we need to create the notebook instance first in SageMaker.
2.	(HO) We will learn how to prepare the data needed for creating a labeling job in AWS.
3.	(HO) We will learn create a new labeling job in AWS console and do it from code.
4.	(HO) We will learn how to process the labeling output for consumption by a model
7.	(P) Finally, we do a quick demo of our labeling pipeline a labeling UI using our custome Bounding-box NER liquid template.

*HO-Hands On
*P-Presentation Slides

### Post-Requisites:
•	After the session’s completion, you should have some data labeled and ready to be used for Model Training.


### Missed it ? Dont Worry
Because Part1 already prepared some labeled data, you should be fine to continue to the next part even if you missed this session.

