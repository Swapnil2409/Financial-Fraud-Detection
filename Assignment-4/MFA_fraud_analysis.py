import pandas as pd
import random
import os

random.seed(42)
os.makedirs("./data", exist_ok=True)

def generate_mfa_fraud_data(n=500):
    mfa_types = ['SMS', 'Authenticator App']
    attack_types = ['Phishing', 'Social Engineering', 'SIM Swap']
    user_errors = ['Clicked malicious link', 'Shared OTP', 'Gave code']
    
    data = []
    for _ in range(n):
        data.append([
            random.choice(mfa_types),
            random.choice(attack_types),
            random.choice(user_errors),
            random.choice([True, False]),
            random.choice([True, False])
        ])
    
    df = pd.DataFrame(data, columns=[
        "mfa_type", "attack_type", "user_error", "fraud_occurred", "transaction_successful"
    ])
    df.to_csv("./data/MFA_Fraud_Analysis_Synthetic.csv", index=False)

generate_mfa_fraud_data()
