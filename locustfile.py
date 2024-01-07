from locust import HttpUser, task, between

class MyLocust(HttpUser):
    wait_time = between(1, 3)
    host = "http://127.0.0.1:5000/numericalintegralservice/0/3.14"  # Replace with the actual URL of your application

    @task(1)  # Adjust the weights as needed
    def numerical_integration_task(self):
        lower = 0
        upper = 3.14159

        # Hit the numerical integration endpoint
        response = self.client.get(f'/numericalintegralservice/{lower}/{upper}')

    @task(2)  # Adjust the weights as needed
    def details_task(self):
        lower = 0
        upper = 3.14159

        # Hit the details endpoint
        response = self.client.get(f'/numericalintegralservice/{lower}/{upper}/details')
