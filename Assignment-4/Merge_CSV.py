import pandas as pd
import glob

# Define the file pattern for all parts
file_pattern = "./data/Synthetic_Financial_datasets_log_part*.csv"

# Find all matching files
csv_files = sorted(glob.glob(file_pattern))

# Merge all CSV files
df_merged = pd.concat([pd.read_csv(f) for f in csv_files], ignore_index=True)

# Save the merged dataset
df_merged.to_csv("./data/Synthetic_Financial_datasets_log.csv", index=False)

print("CSV files successfully merged into Synthetic_Financial_datasets_log.csv")
