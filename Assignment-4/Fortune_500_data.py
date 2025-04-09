import pandas as pd
import numpy as np
import random
import os

random.seed(42)
os.makedirs("./data", exist_ok=True)

def generate_fortune500_data(n=100):
    systems = ['Legacy', 'Hybrid', 'AI-Powered']
    data = []
    
    for _ in range(n):
        system = random.choice(systems)
        if system == 'AI-Powered':
            detection = round(np.random.uniform(0.85, 0.95), 2)
            prevention = round(detection - np.random.uniform(0.05, 0.1), 2)
            trust = round(np.random.uniform(4.5, 5.0), 2)
        elif system == 'Hybrid':
            detection = round(np.random.uniform(0.6, 0.8), 2)
            prevention = round(detection - np.random.uniform(0.05, 0.1), 2)
            trust = round(np.random.uniform(3.5, 4.5), 2)
        else:  # Legacy
            detection = round(np.random.uniform(0.3, 0.6), 2)
            prevention = round(detection - np.random.uniform(0.1, 0.15), 2)
            trust = round(np.random.uniform(2.0, 3.5), 2)
        
        data.append([
            f"CMP-{random.randint(100000, 999999)}",
            system,
            detection,
            prevention,
            trust
        ])
    
    df = pd.DataFrame(data, columns=[
        "Company_ID", "Fraud_Detection_System", "Fraud_Detection_Rate",
        "Fraud_Prevention_Rate", "Customer_Trust_Score"
    ])
    df.to_csv("./data/Fortune500_Fraud_Analysis_Updated.csv", index=False)

generate_fortune500_data()
