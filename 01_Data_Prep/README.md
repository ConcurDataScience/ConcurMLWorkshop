Day 2 Part1:

Welcome to the Data Prep section of the ML Workshop, in this section, you would get a sense of how we acquire data, prep it, ETL it, and get it ready for consumption and to begin our Model Development part of Data Science.

Pre-Requisites:
1.	You should have created an AWS account and verified some of the key access to key resources we will be using in this 4 day’s workshop
2.	You have created an IAM role that you will be using in this series, with the necessary permissions
3.	You have created an S3 notebook and can access the git repo shared earlier.
4.	You have downloaded the data into that S3 bucket.

Key Objectives:
By the end of this section, you should have a good idea on 
1.	How to data prep using Pyspark, Glue Sagemakerr, Glue Script Processor.
2.	How Glue crawler’s work
3.	How data gets to Athena and how to Query data via Athena

Steps We will go through:
1.	(HO) Before we dive deep into Mechanics, let’s create a Glue Endpoint and Glue Notebook for our script creation and testing
2.	(P) We will learn some key concepts around how we process data and store it in a GDPR compliant way, and also learn some of the key AWS resources we use in our Data Engineering Pipeline in Production
3.	(HO) Then we will experiment with our script creation in a notebook-like environment but with Spark Enabled.
4.	HO) Now that we are ready, we will convert it into a script so it can run on its own
5.	(HO) Then we will schedule it via a trigger.
6.	(HO) Then we will create a Glue crawler to crawl the output generated so far
7.	(HO) Finally, we will look at Athena and query some data to see how it all works.

*HO-Hands On
*P-Presentation Slides

Post-Requisites:
•	After the session’s completion, you should have an output file location that is pre-processed and ready to be used for Model Training.
•	You should be having a crawler that would have crawled that data and created an Athena Table.



If you missed this session:
Please download the Final Dataset, create a glue crawler, crawl the data, and make sure Athena's table is having the data by querying it.

