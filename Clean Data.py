# ==========================================
# Day 3: Clean Data
# ==========================================

import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv")  # change if needed

print("🧹 Day 3: Cleaning Data...\n")

# -------------------------------
# 1. Check Missing Values
# -------------------------------
print("🔹 Missing Values Before Cleaning:\n")
print(df.isnull().sum())

print("\n" + "="*50)

# -------------------------------
# 2. Handle Missing Values
# -------------------------------

# Fill numeric columns with 0
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
df[numeric_cols] = df[numeric_cols].fillna(0)

# Fill categorical columns with 'Unknown'
categorical_cols = df.select_dtypes(include=['object']).columns
df[categorical_cols] = df[categorical_cols].fillna('Unknown')

print("✅ Missing values handled!\n")

print("🔹 Missing Values After Cleaning:\n")
print(df.isnull().sum())

print("\n" + "="*50)

# -------------------------------
# 3. Remove Duplicates
# -------------------------------
duplicates_before = df.duplicated().sum()
print(f"🔹 Duplicate Rows Before: {duplicates_before}")

df.drop_duplicates(inplace=True)

duplicates_after = df.duplicated().sum()
print(f"🔹 Duplicate Rows After: {duplicates_after}")

print("\n" + "="*50)

# -------------------------------
# 4. Fix Data Types (Optional)
# -------------------------------

# Example: convert column to numeric (if needed)
# df['Total_Sales'] = pd.to_numeric(df['Total_Sales'], errors='coerce')

# Example: convert date column (if exists)
# df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

print("✅ Data types checked (modify if needed)")

print("\n" + "="*50)

# -------------------------------
# 5. Save Cleaned Data (Optional)
# -------------------------------
df.to_csv("cleaned_sales_data.csv", index=False)

print("💾 Cleaned data saved as cleaned_sales_data.csv")

print("\n✅ Day 3 Completed!")