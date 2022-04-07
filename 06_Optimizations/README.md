# Performance tunning class

## Summary

This class shows how to tune up your service and model serving to handle more load. The first part of the lesson contains a simulation of load tests to see what our service can handle. The next steps take us through an analysis of the load and multiple ways how to handle the load.

## Introduction
1. Why care about performance?
2. What are the options?
3. What is [Locust](https://locust.io/)?
4. What is [TensorFlow Serving](https://www.tensorflow.org/tfx/serving/architecture)?


## Tasks
**1. Start the service from within the container**
This task verifies that we can start where the previous class ended and that we have everything running.

**2. Run the first load test**
This task is the MOST important one because the locust is used also in other tasks. Expect to see results of what our current service can handle.

**3. Optimize logs**
You can't enhance it without properly measuring it, therefore we are going to modify the logging in our service.

**4. Swap to TF Serving**
The step where move the model inference to tf-serving and check whether everything works as expected.

**5. Performance tuning**
The last step allows us to play with the tf-serving configuration to achieve the highest possible throughput.


## Implementation steps

### Pre-requisites
The code from previous lesson `05_Service_Building`

### 1. Start the service from within the container
This task verifies that we can start where the previous class ended and that we have everything running.
#### Steps
1. **IMPORTANT:** Please make sure that your working dir is `start_version` directory.
2. Check/Get latest version of code: 
   ```bash
   git pull
   ```
3. Copy final state of previous lesson to current dir [05_Service_Building/full_service](https://github.com/ConcurDataScience/ConcurMLWorkshop/tree/main/05_Service_Building/full_service) code.
   ```bash
   cp -r ../../05_Service_Building/full_service full_service
   ```
4. get/build a docker image from the previous lesson
   ```bash
   docker build ./full_service -t mlservice  
   ```
5. start the docker and send it to background
   ```bash
   docker run -p 8080:8080 mlservice:latest &
   ```
6. optional step if case of error `Bind for 0.0.0.0:8080 failed: port is already allocated.`
   1. Check which process it using the port
   ```bash
   lsof -i :8080
   ```
   1. Stop all running docker images 
   ```bash
   docker kill $(docker ps -q)
   ```
7. test that the service is running and responsive via postman or following code
   1. curl
   ```bash
   curl --location --request POST 'http://127.0.0.1:8080/predict' \
   --header 'Content-Type: application/json' \
   --data-raw '{"text": "That is really a interesting service"}'
   ```
   2. python   
   ```python
   import requests
   import json

   url = "http://127.0.0.1:8080/predict"

   payload = json.dumps({
      "text": "I had an excellent service"
   })
   headers = {
      'Content-Type': 'application/json'
   }

   response = requests.request("POST", url, headers=headers, data=payload)
   print(response.text)
   ```

### 2. Run the first load test
This task is the MOST important one because the locust is used also in other tasks. Expect to see results of what our current service can handle.

#### Steps
1. Create the first locustfile.py for testing the service ( documentation: http://docs.locust.io/en/stable/quickstart.html ). We are borrowing the payload body from the postman example.   
   ```python
   from locust import HttpUser, task, between
   import json

   class ModelServiceUser(HttpUser):
      @task
      def test_task(self):
         payload = json.dumps(
               {"text": "I have an excellent service!"})
         headers = {'Content-Type': 'application/json'}

         self.client.post(url="/predict",
                           headers=headers,
                           data=payload,
                           )    

   ```
2. Install locust
   ```bash
   pip install locust
   ```
3. Run the locust server from command line so that it offers by default testing locally running service with user spawn rate of 1 user/sec and max 100users.
   ```bash
   locust --host http://127.0.0.1:8080 --users 100 --spawn-rate 1   
   ```
5. Run the first test and observe/print screen/save results:
   1. max responses per minute
   2. the model & service behavior
   3. the existence of logs that would explain why the call takes so long

### 3. Optimize logs 
You can't enhance it without properly measuring it, therefore we are going to modify the logging in our service.

#### Steps
1. Go to main.py and replace `logging.basicConfig(level=logging.INFO)` with 
   ```python
   logging.basicConfig(filename='debug.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
   ```
2. Go to service -> endpoints.py
3. Add following imports 
   ```python
   import time
   import logging
   ```
4. Wrap inference with timing info
   ```python
   start = time.time()
   keras_predictions = model.predict(predict_texts_to_sequences)
   logging.info(f'Inference took: {time.time()-start}sec')
   ```
5. Stop running docker, rebuild it with latest version of code and start again
   ```bash
   docker kill $(docker ps -q)
   docker build ./full_service -t mlservice
   docker run -p 8080:8080 mlservice:latest &
   ```
6. Run the load test once more time
   ```bash
   locust --host http://127.0.0.1:8080 --users 100 --spawn-rate 1
   ```
7. Connect to running docker
   1. simple approach -> Visual Studio Code -> Docker tab -> right click on running instance -> `Attach Shell`
   2. manual approach
   ```bash
   # get container id
   docker ps

   # connect to running docker 
   docker exec -it <CONTAINER ID> /bin/bash
   ```
8. Check logs
   ```bash
   # -f means follow so it keeps showing any incoming logs
   # swap '-f' from '-n 1000' to see last 1000rows
   tail -f debug.log
   ```

### 4. Swap to TF Serving
The step where move the model inference to tf-serving and check whether everything works as expected.

#### Steps
1. **!!! IMPORTANT !!!** 
   1. Rename folder `model/v1` to `model/1`
   ```bash
   mv full_service/model/v1 full_service/model/1
   ```
   2. Change path to model in main.py
   ```python
   #### change following lines
   # _MODEL_PATH = './model/v1'
   # _TOKENIZER_PATH = './model/v1/keras_tokenizer.json'
   #### to:
   _MODEL_PATH = './model/1'
   _TOKENIZER_PATH = './model/1/keras_tokenizer.json'
   ```
2. Find in the Docker file following line `RUN apt-get install -y curl python3 python3-pip` and below following code for tf-serving setup (https://www.tensorflow.org/tfx/serving/setup)
   ```docker
   # Install tf-serving
   RUN echo "deb [arch=amd64] http://storage.googleapis.com/tensorflow-serving-apt stable tensorflow-model-server tensorflow-model-server-universal" | tee /etc/apt/sources.list.d/tensorflow-serving.list && \
      curl https://storage.googleapis.com/tensorflow-serving-apt/tensorflow-serving.release.pub.gpg | apt-key add -
   RUN  apt-get update && apt-get install -y tensorflow-model-server
   ```
3. Stop running docker, rebuild it with latest version of code and start again
   ```bash
   docker kill $(docker ps -q) &&\
   docker build ./full_service -t mlservice &&\
   docker run -p 8080:8080 mlservice:latest &
   ```
4. Let's verify that TF Serving is correctly installed by:
   1. Connect to docker @see task3.7
   2. Start the server 
   ```bash
   tensorflow_model_server --port=8500 --rest_api_port=8501 --model_base_path=/app/model/ --model_name=model &
   ```
   3. Do inference request to server 
   ```bash
   curl --location --request POST 'http://localhost:8501/v1/models/model/versions/1:predict' --header 'Content-Type: application/json'  --data-raw '{"inputs": [[18.0,  64.0, 137.0, 163.0,   0.0]]}'
   ```
5. If everything is working then it is time to redirect our service to TF-Serving. There is need to modify way how we execute inference. 
   1. Add following code to `service.endpoints.py`:
      ```python
      import requests
      import json
      def _tf_predict(inputs):
         url = "http://127.0.0.1:8501/v1/models/model/versions/1:predict"

         data = list(inputs[0].astype(float))    
         payload = json.dumps({"inputs": [data]})    
         headers = {'Content-Type': 'application/json'}

         response = requests.request("POST", url, headers=headers, data=payload)
         json_data = response.json()

         return np.array(json_data['outputs'])
      ```
   2. Change inference line to call out new method:
      ```python
      ## original line
      # keras_predictions = model.predict(predict_texts_to_sequences)
      
      keras_predictions = _tf_predict(predict_texts_to_sequences)
      ```
6. Modify the docker code to start automatically the tf-serving server by modifying lines in the file `start.sh`. 
   ```bash   
   #!/bin/bash

   # Start the TF Serving
   exec tensorflow_model_server --port=8500 --rest_api_port=8501 --model_base_path=/app/model/ --model_name=model &

   # Start the Flask service
   exec python3 /app/main.py
   ```
7. Stop running docker, rebuild it with latest version of code and start again. @see comands in step 3.
8. Run the load test via locust
    ```bash
   locust --host http://127.0.0.1:8080 --users 100 --spawn-rate 1
   ```

### 5. Performance tuning
The last step allows us to play with the tf-serving configuration to achieve the highest possible throughput.

#### Steps
1. Create file `full_service/tf-serving-batching-parameters.txt` with following batch inference config
   ```
   max_batch_size { value: 16 }
   batch_timeout_micros { value: 0 }
   max_enqueued_batches { value: 10000 }
   num_batch_threads { value: 2 }
   pad_variable_length_inputs: true
   ```
2. Modify tf-serving to start with batch configuration
   1. change command in the `start.sh` to:
   ```bash
   exec tensorflow_model_server --port=8500 --rest_api_port=8501 \
                                --model_base_path=/app/model/ \
                                --model_name=model  \
                                --enable_batching=true \
                                --batching_parameters_file="/app/tf-serving-batching-parameters.txt" &
   ```
   2. Stop running docker, rebuild it with latest version of code and start again. @see comands in step 3.
3. Run the load test via locust
    ```bash   
   locust --host http://127.0.0.1:8080 --users 100 --spawn-rate 1
   ```
4. Experiment with increasing the batch size
   1. Optional: for simplicity the test can be done via direct connection to running Docker. *Keep in mind that any change inside docker **will NOT** survive Docker rebuild!!!*
5. Experiment with min/max waiting time
6. Extras:
   ```bash
   # to observe pure inference times for service
   tail debug.log -n 100 | grep Inference

   # to see which process is using the most CPU
   top
   ```
   
# Summary
This is just a beginning and there many more ways how to tune your setup.

