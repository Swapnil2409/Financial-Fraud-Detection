import pandas as pd
import numpy as np
import random
from faker import Faker
import os

# Setup
fake = Faker()
np.random.seed(42)
random.seed(42)
os.makedirs("./data", exist_ok=True)

def generate_ontario_fraud_data(n=1000):
    fraud_types = ['Online Shopping', 'Identity Fraud', 'Investment Scam', 'Phishing', 'Credit Card Fraud']
    channels = ['phone', 'email', 'in-person', 'web']
    
    data = []
    for _ in range(n):
        is_preventable = random.choice([True, False])
        detected_at = 'Initiation' if is_preventable else 'Completion'
        data.append([
            f"FRAUD-{random.randint(1000000, 9999999)}",
            random.choice(fraud_types),
            'Ontario',
            fake.date_between(start_date='-1y', end_date='today'),
            round(np.random.uniform(500, 10000), 2),
            random.choice(['victim', 'employer', 'police']),
            random.randint(18, 80),
            random.choice(channels),
            is_preventable,
            detected_at,
            round(np.random.uniform(0.1, 0.95), 2)
        ])
    df = pd.DataFrame(data, columns=[
        "fraud_id", "fraud_type", "location", "date_reported", "amount_loss",
        "reported_by", "age", "channel", "is_preventable", "fraud_detected_at", "risk_score"
    ])
    df.to_csv("./data/synthetic_fraud_ontario_v3.csv", index=False)

generate_ontario_fraud_data()
