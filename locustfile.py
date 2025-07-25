from locust import HttpUser, task, between

class MystressTestuser(HttpUser):
    wait_time = between(1, 2)

    @task
    def my_task(self):
        self.client.get("/some-endpoint")