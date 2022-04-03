from locust import HttpUser, task, between
import json

class ModelServiceUser(HttpUser):
    @task
    def test_task(self):
        payload = json.dumps(
            {"text": "That is a really bad service, I hate it!"})
        headers = {'Content-Type': 'application/json'}

        self.client.post(url="/predict",
                         headers=headers,
                         data=payload,
                         )    
