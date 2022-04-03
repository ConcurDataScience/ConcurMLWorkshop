# Performance tunning class

## Summary

This class shows how to tune up your service and model serving to handle more load. The first part of the lesson contains a simulation of load tests to see what our service can handle. The next steps take us through an analysis of the load and multiple ways how to handle the load.

## Pre-requisite
1. code from previous lesson `05_Service_Building`

## Tasks
### 1. Start the service from within the container
This task verifies that we start from the same point.

#### Steps
1. Get [05_Service_Building/full_service](https://github.com/ConcurDataScience/ConcurMLWorkshop/tree/main/05_Service_Building/full_service) code.
2. get/build a docker image from the previous lesson
3. run command: `docker run -p 8080:8080 -it mlservice:latest /bin/bash`
4. start service: `python3 main.py`
5. test that the service is running and responsive via postman 

### 2. Run the first load test
This task is the MOST important one because the locust is used also in other tasks. Expect to see results of what our current service can handle.

#### Steps
1. Create the first locustfile.py for testing the service ( documentation: http://docs.locust.io/en/stable/quickstart.html ). Borrow the payload body from the postman example.   
2. Run the locust server and set the server to `http://127.0.0.1:8080`
3. Run the first test and observe:
   1. max responses per minute
   2. the model & service behavior
   3. the existence of logs that would explain why the call takes so long

### 3. Optimize logs 
You can't enhance it without properly measuring it, therefore we are going to modify the logging in our service.

#### Steps
1. Add need logs to a service call to cover preprocessing & inference
2. Run the load test once more time
3. Check if the logs help to explain at least 95% of service call time

### 4. Swap to TF Serving
The step where move the model inference to tf-serving and check whether everything works as expected.

#### Steps
1. Modify service code to call tf-serving
2. Modify the docker code to start the tf-serving server for you
3. Run the load test 

### 5. Performance tuning
The last step allows us to play with the tf-serving configuration to achieve the highest possible throughput.

#### Steps
4. Add code for starting the tf-serving with batch configuration
5. Experiment with increasing the batch size
6. Experiment with min/max waiting time
