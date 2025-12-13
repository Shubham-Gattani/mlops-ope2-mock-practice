from locust import HttpUser, task, between
import random

# Generate a single random transaction payload
def random_transaction():
    return {
        "Time": random.uniform(0, 100000),
        "Amount": random.uniform(1, 500),

        # The PCA features V1–V28 (random dummy values)
        **{f"V{i}": random.uniform(-5, 5) for i in range(1, 29)}
    }


class FraudAPIUser(HttpUser):
    wait_time = between(0.1, 0.5)  # Short wait time to generate load

    @task
    def predict_fraud(self):
        payload = random_transaction()
        self.client.post("/predict", json=payload)