:calendar: 
## Day 2 Part 1:

Welcome to the Data Prep section of the ML Workshop, in this section, you would get a sense of how we acquire data, prep it, ETL it, and get it ready for consumption and to begin our Model Development part of Data Science.

## Pre-Requisites:
1.	You should have created an AWS account and verified some of the key access to key resources we will be using in this 4 day’s workshop
2.	You have created an IAM role that you will be using in this series, with the necessary permissions
3.	You have created an S3 bucket and can access the git repo shared earlier.

## Key Objectives:
By the end of this section, you should have a good idea on 
1.	How to data prep using Pyspark, Glue Sagemakerr, Glue Script Processor.
2.	How Glue crawler’s work
3.	How data gets to Athena and how to Query data via Athena

## Steps We will go through:
1.	(HO) Before we dive deep into Mechanics, let’s create a Glue Endpoint and Glue Notebook for our script creation and testing ( This takes Approx 6 min each)
2.	(P) We will learn some key concepts around how we process data and store it in a GDPR compliant way, and also learn some of the key AWS resources we use in our Data Engineering Pipeline in Production
3.	(HO) Then we will experiment with our script creation in a notebook-like environment but with Spark Enabled.
4.	(HO) Now that we are ready, we will convert it into a script so it can run on its own
5.	(HO) Then we will schedule it via a trigger.
6.	(HO) Then we will create a Glue crawler to crawl the output generated so far
7.	(HO) Finally, we will look at Athena and query some data to see how it all works.

*HO-Hands On
*P-Presentation Slides

## Post-Requisites:
•	After the session’s completion, you should have an output file location that is pre-processed and ready to be used for Model Training.
•	You should be having a Enrich crawler that would have crawled that Enrich data and created an Athena Table.


## Missed it? Dont Worry 
If you missed this session:
Please follow below steps:
1. Download the Final Dataset enriched_data.tar.gz from https://github.com/ConcurDataScience/ConcurMLWorkshop/blob/main/01_Data_Prep/enriched_data.tar.gz
2. Untar it using either a UI unzip software or below command:

`tar -xf enriched_data.tar.gz`

As shown below:
<img width="603" alt="Screen Shot 2022-04-01 at 11 34 39 AM" src="https://user-images.githubusercontent.com/101754067/161324337-a2f9f89f-cba3-4fcc-ac4d-85757665ba56.png">

3.  Now, upload this enriched_data folder to S3 bucket that you created on first day. ( Ths uplaod can take up to 5 mins depending on internet upload speed) - Be patient

<img width="883" alt="Screen Shot 2022-04-01 at 11 35 24 AM" src="https://user-images.githubusercontent.com/101754067/161324429-f9d54ae9-25df-4721-951c-8e3c4d7cc5b8.png">

<img width="845" alt="Screen Shot 2022-04-01 at 11 35 36 AM" src="https://user-images.githubusercontent.com/101754067/161324454-b9461a66-a641-4305-9032-b029066efc7b.png">

<img width="853" alt="Screen Shot 2022-04-01 at 11 35 46 AM" src="https://user-images.githubusercontent.com/101754067/161324474-e952cb2d-dbd5-4d33-98b1-e782f5fe4015.png">

<img width="1555" alt="Screen Shot 2022-04-01 at 11 36 12 AM" src="https://user-images.githubusercontent.com/101754067/161324492-fa2936be-da22-41af-b519-bb688e3c40a9.png">

<img width="1375" alt="Screen Shot 2022-04-01 at 11 37 49 AM" src="https://user-images.githubusercontent.com/101754067/161324500-fb28fc86-9c10-42a5-99b7-4cd3cc022010.png">

4.  Also, make sure you have enriched_data and athena_log two folders in the s3 bucket. 
 <img width="1603" alt="Screen Shot 2022-04-01 at 11 43 25 AM" src="https://user-images.githubusercontent.com/101754067/161324577-6c3753f9-4c4d-49d3-946b-beb219baf591.png">
 
5.  Now lets go to Glue and select Glue crawler

<img width="1198" alt="Screen Shot 2022-04-01 at 11 38 08 AM" src="https://user-images.githubusercontent.com/101754067/161324725-d3b62b19-851b-473b-a6cb-4390a9458e0c.png">

<img width="649" alt="Screen Shot 2022-04-01 at 11 38 45 AM" src="https://user-images.githubusercontent.com/101754067/161324944-4232541e-e48c-4ea9-9c73-bfd024d201a5.png">

<img width="894" alt="Screen Shot 2022-04-01 at 11 38 59 AM" src="https://user-images.githubusercontent.com/101754067/161324951-2128c946-3657-45c1-85c0-814fa6e8306d.png">

<img width="621" alt="Screen Shot 2022-04-01 at 11 39 12 AM" src="https://user-images.githubusercontent.com/101754067/161324969-057a43d7-5062-4aa8-9c61-7fd73c9c890f.png">


6. Lets give the s3 location that glue will crawl:


 <img width="639" alt="Screen Shot 2022-04-01 at 11 39 19 AM" src="https://user-images.githubusercontent.com/101754067/161325009-4fc2bff3-97ac-4276-8ae7-ab05c1a872c2.png">
 
 
 <img width="485" alt="Screen Shot 2022-04-01 at 11 39 24 AM" src="https://user-images.githubusercontent.com/101754067/161325031-427a59e4-1a97-4308-92c6-2d619c6dd3c1.png">
 
 
7. Select the Role that you created in first day. 

 <img width="685" alt="Screen Shot 2022-04-01 at 11 39 31 AM" src="https://user-images.githubusercontent.com/101754067/161325069-1e4708d7-1da4-4e09-82d9-7c03ce49465b.png">
 
8. Now you will see this error: "No database"

<img width="627" alt="Screen Shot 2022-04-01 at 11 39 43 AM" src="https://user-images.githubusercontent.com/101754067/161325119-3d109f0d-3712-4c6b-a39c-b902774a8000.png">

So lets create one 

<img width="551" alt="Screen Shot 2022-04-01 at 11 40 08 AM" src="https://user-images.githubusercontent.com/101754067/161325157-a01c3ddc-68bf-4c61-94f3-06105d221556.png">

The Summary looks like this:

<img width="1276" alt="Screen Shot 2022-04-01 at 11 40 21 AM" src="https://user-images.githubusercontent.com/101754067/161325182-0a880c06-c8d8-4c29-8d48-3274deb5895c.png">

9.  Lets Run the glue crawler

<img width="1312" alt="Screen Shot 2022-04-01 at 11 40 31 AM" src="https://user-images.githubusercontent.com/101754067/161325234-16df802d-3022-4872-b687-8377f7e24806.png">

<img width="1299" alt="Screen Shot 2022-04-01 at 11 40 46 AM" src="https://user-images.githubusercontent.com/101754067/161325250-be138537-8938-47a6-8863-7b8e3e055936.png">

Finally the Glue crawler should stop in 1 min:

<img width="1289" alt="Screen Shot 2022-04-01 at 11 41 35 AM" src="https://user-images.githubusercontent.com/101754067/161325291-7d7a6ab8-d032-453b-bbb9-8ef3fac7e5ed.png">

10.  Lets now go to DB and select the DB->Table and see the table structure

<img width="714" alt="Screen Shot 2022-04-01 at 11 41 43 AM" src="https://user-images.githubusercontent.com/101754067/161325351-d0bfa376-5fe8-49a3-8b9c-8ef61e9e7093.png">

<img width="1005" alt="Screen Shot 2022-04-01 at 11 41 48 AM" src="https://user-images.githubusercontent.com/101754067/161325360-b5602457-4187-4499-893f-0e014071c6c0.png">

Click on "View Data"

<img width="1241" alt="Screen Shot 2022-04-01 at 11 41 55 AM" src="https://user-images.githubusercontent.com/101754067/161325398-b998c2fe-98a2-4506-afbe-81591d798e95.png">

Now you will see this error: 

<img width="1201" alt="Screen Shot 2022-04-01 at 11 42 49 AM" src="https://user-images.githubusercontent.com/101754067/161325505-068e3f09-9e5a-4aeb-bcca-0c7f9c9d54e2.png">

11.  Now, Lets configure athena to send logs to athena_logs directory created initially
12.  
<img width="919" alt="Screen Shot 2022-04-01 at 11 43 02 AM" src="https://user-images.githubusercontent.com/101754067/161325517-db33e2a5-4911-449e-a9c0-78b208bb8d4b.png">
<img width="1603" alt="Screen Shot 2022-04-01 at 11 43 25 AM" src="https://user-images.githubusercontent.com/101754067/161325540-d4c3b867-3c18-4698-8185-fd57e6a0318f.png">

12.  Lets now execute an athena Query.

<img width="1542" alt="Screen Shot 2022-04-01 at 11 43 40 AM" src="https://user-images.githubusercontent.com/101754067/161325563-fbae7b32-6d16-4076-afe1-7521fb0a2349.png">

16.  Viola! you are all set! 

<img width="1139" alt="Screen Shot 2022-04-01 at 11 43 49 AM" src="https://user-images.githubusercontent.com/101754067/161325602-1d75d5e4-0e8d-431c-b2a3-cddcc90295a3.png">

