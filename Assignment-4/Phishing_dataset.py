import pandas as pd
import random
import os

random.seed(42)
os.makedirs("./data", exist_ok=True)

def generate_phishing_mfa_data(n=500):
    phishing_types = ['Email', 'SMS', 'Social Media']
    mfa_types = ['SMS', 'Authenticator App']
    user_errors = ['Clicked malicious link', 'Shared OTP/code', 'Reused password']
    industries = ['Banking', 'Retail', 'Healthcare', 'Government', 'Education']
    stages = ['Initiation', 'Completion']
    
    data = []
    for _ in range(n):
        data.append([
            random.choice(phishing_types),
            random.choice(mfa_types),
            random.choice(user_errors),
            random.choice([True, False]),
            random.choice(stages),
            random.choice([True, False]),
            random.randint(1, 5),
            random.choice(industries)
        ])
    
    df = pd.DataFrame(data, columns=[
        "phishing_type", "mfa_type", "user_error", "fraud_occurred",
        "transaction_stage", "transaction_successful",
        "user_awareness_score", "industry"
    ])
    df.to_csv("./data/synthetic_phishing_mfa_dataset.csv", index=False)

generate_phishing_mfa_data()
