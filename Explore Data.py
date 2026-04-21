# ==========================================
# Day 2: Explore Data
# ==========================================

import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv")  # change if needed

print("📊 Day 2: Exploring Data...\n")

# -------------------------------
# 1. View First Rows
# -------------------------------
print("🔹 First 5 Rows:\n")
print(df.head())

print("\n" + "="*50)

# -------------------------------
# 2. Dataset Shape
# -------------------------------
print("\n🔹 Shape (Rows, Columns):")
print(df.shape)

print("\n" + "="*50)

# -------------------------------
# 3. Column Names
# -------------------------------
print("\n🔹 Columns:")
print(df.columns.tolist())

print("\n" + "="*50)

# -------------------------------
# 4. Data Types & Info
# -------------------------------
print("\n🔹 Data Info:")
df.info()

print("\n" + "="*50)

# -------------------------------
# 5. Basic Statistics
# -------------------------------
print("\n🔹 Statistical Summary:")
print(df.describe())

print("\n" + "="*50)

# -------------------------------
# 6. Check Missing Values
# -------------------------------
print("\n🔹 Missing Values:")
print(df.isnull().sum())

print("\n" + "="*50)

# -------------------------------
# 7. Unique Values (for understanding categories)
# -------------------------------
print("\n🔹 Unique Values Per Column:\n")
for col in df.columns:
    print(f"{col}: {df[col].nunique()} unique values")

print("\n" + "="*50)

print("\n✅ Day 2 Completed!")