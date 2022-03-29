:calendar: 
### Day 2 Part 1:

Welcome to the Data Prep section of the ML Workshop, in this section, you would get a sense of how we acquire data, prep it, ETL it, and get it ready for consumption and to begin our Model Development part of Data Science.

### Pre-Requisites:
1.	You should have created an AWS account and verified some of the key access to key resources we will be using in this 4 day’s workshop
2.	You have created an IAM role that you will be using in this series, with the necessary permissions
3.	You have created an S3 bucket and can access the git repo shared earlier.

### Key Objectives:
By the end of this section, you should have a good idea on 
1.	How to data prep using Pyspark, Glue Sagemakerr, Glue Script Processor.
2.	How Glue crawler’s work
3.	How data gets to Athena and how to Query data via Athena

### Steps We will go through:
1.	(HO) Before we dive deep into Mechanics, let’s create a Glue Endpoint and Glue Notebook for our script creation and testing ( This takes Approx 6 min each)
2.	(P) We will learn some key concepts around how we process data and store it in a GDPR compliant way, and also learn some of the key AWS resources we use in our Data Engineering Pipeline in Production
3.	(HO) Then we will experiment with our script creation in a notebook-like environment but with Spark Enabled.
4.	(HO) Now that we are ready, we will convert it into a script so it can run on its own
5.	(HO) Then we will schedule it via a trigger.
6.	(HO) Then we will create a Glue crawler to crawl the output generated so far
7.	(HO) Finally, we will look at Athena and query some data to see how it all works.

*HO-Hands On
*P-Presentation Slides

### Post-Requisites:
•	After the session’s completion, you should have an output file location that is pre-processed and ready to be used for Model Training.
•	You should be having a Enrich crawler that would have crawled that Enrich data and created an Athena Table.


### Missed it? Dont Worry 
If you missed this session:
Please follow below steps:
1. Download the Final Dataset from enriched_data.tar.gz, untar it, and upload it in s3:://{bucket_name}/labeling_data_component/data_prep_output/enriched_data
2. Create a glue crawler as described https://docs.aws.amazon.com/glue/latest/dg/crawler-configuration.html
3. Crawl the data ( Run crawler)
4. Make sure Athena's table is having the data by querying it. ( Check the database-> Tables-> View Data)

