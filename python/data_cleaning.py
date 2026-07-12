import pandas as pd
from db_connection import engine

# Load data from MySQL
df = pd.read_sql("SELECT * FROM customer", engine)

print("=" * 50)
print("Dataset Loaded Successfully")
print("=" * 50)

# Dataset Shape
print("\nDataset Shape:")
print(df.shape)

# Dataset Information
print("\nDataset Information:")
print(df.info())

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate Records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Convert TotalCharges to Numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Fill Missing Values
df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Save Clean Dataset
df.to_csv("dataset/clean_customer_churn.csv", index=False)

print("\n✅ Clean dataset saved successfully!")