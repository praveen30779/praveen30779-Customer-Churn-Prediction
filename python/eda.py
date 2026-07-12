import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from db_connection import engine

# Create output folder automatically
os.makedirs("output/charts", exist_ok=True)

# Load data from MySQL
df = pd.read_sql("SELECT * FROM customer", engine)

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())

print("=" * 50)
print("EDA Started")
print("=" * 50)

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nSummary Statistics:")
print(df.describe())

# ==========================
# Chart 1 : Churn Distribution
# ==========================
plt.figure(figsize=(6,5))
df["Churn"].value_counts().plot(kind="bar")
plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("output/charts/churn_distribution.png")
plt.close()

# ==========================
# Chart 2 : Gender vs Churn
# ==========================
pd.crosstab(df["gender"], df["Churn"]).plot(kind="bar", figsize=(6,5))
plt.title("Gender vs Churn")
plt.tight_layout()
plt.savefig("output/charts/gender_vs_churn.png")
plt.close()

# ==========================
# Chart 3 : Senior Citizen vs Churn
# ==========================
pd.crosstab(df["SeniorCitizen"], df["Churn"]).plot(kind="bar", figsize=(6,5))
plt.title("Senior Citizen vs Churn")
plt.tight_layout()
plt.savefig("output/charts/seniorcitizen_vs_churn.png")
plt.close()

# ==========================
# Chart 4 : Contract vs Churn
# ==========================
pd.crosstab(df["Contract"], df["Churn"]).plot(kind="bar", figsize=(7,5))
plt.title("Contract vs Churn")
plt.tight_layout()
plt.savefig("output/charts/contract_vs_churn.png")
plt.close()

# ==========================
# Chart 5 : Internet Service vs Churn
# ==========================
pd.crosstab(df["InternetService"], df["Churn"]).plot(kind="bar", figsize=(7,5))
plt.title("Internet Service vs Churn")
plt.tight_layout()
plt.savefig("output/charts/internet_service_vs_churn.png")
plt.close()

# ==========================
# Chart 6 : Payment Method vs Churn
# ==========================
pd.crosstab(df["PaymentMethod"], df["Churn"]).plot(kind="bar", figsize=(10,5))
plt.title("Payment Method vs Churn")
plt.tight_layout()
plt.savefig("output/charts/payment_method_vs_churn.png")
plt.close()

# ==========================
# Chart 7 : Monthly Charges
# ==========================
plt.figure(figsize=(7,5))
plt.hist(df["MonthlyCharges"], bins=30)
plt.title("Monthly Charges Distribution")
plt.xlabel("Monthly Charges")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("output/charts/monthly_charges_distribution.png")
plt.close()

# ==========================
# Chart 8 : Tenure
# ==========================
plt.figure(figsize=(7,5))
plt.hist(df["tenure"], bins=30)
plt.title("Tenure Distribution")
plt.xlabel("Tenure")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("output/charts/tenure_distribution.png")
plt.close()

# ==========================
# Chart 9 : Correlation Heatmap
# ==========================
plt.figure(figsize=(8,6))
numeric_df = df.select_dtypes(include=["int64", "float64"])
sns.heatmap(numeric_df.corr(), annot=True, cmap="Blues")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("output/charts/correlation_heatmap.png")
plt.close()

print("\n✅ All EDA charts generated successfully!")
print("📁 Saved in: output/charts/")
