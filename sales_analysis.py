# ==========================================
# Sales Data Analysis - Day 1
# Setup & Load Data
# ==========================================

import pandas as pd

print("🚀 Starting Sales Data Analysis...\n")

# Load CSV File
try:
    file_name = "sales_data.csv"   # change to "sales_data.csv" if renamed
    df = pd.read_csv(file_name) 
    print("✅ Dataset loaded successfully!\n")

except FileNotFoundError:
    print("❌ Error: File not found! Check file name and location.")
    exit()

except Exception as e:
    print("❌ Error while loading file:", e)
    exit()


# Display First Rows
print("📊 First 5 Rows:\n")
print(df.head())

print("\n" + "="*50)

# Dataset Info
print("\n📐 Shape (Rows, Columns):")
print(df.shape)

print("\n📋 Column Names:")
print(df.columns.tolist())

print("\n🔍 Data Info:")
print(df.info())

print("\n📈 Basic Statistics:")
print(df.describe())

print("\n" + "="*50)

# Missing Values
print("\n⚠️ Missing Values:")
print(df.isnull().sum())

print("\n✅ Day 1 Completed Successfully!")