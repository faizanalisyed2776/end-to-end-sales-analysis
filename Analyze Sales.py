# ==========================================
# Day 4: Analyze Sales
# ==========================================

import pandas as pd

# Load cleaned dataset (recommended)
df = pd.read_csv("cleaned_sales_data.csv")  # or "sales_data.csv"

print("📈 Day 4: Sales Analysis...\n")

# -------------------------------
# Column Names (EDIT if needed)
# -------------------------------
sales_column = "Total_Sales"   # change if your column name is different
product_column = "Product"     # change if needed

# -------------------------------
# 1. Total Revenue
# -------------------------------
total_revenue = df[sales_column].sum()
print(f"💰 Total Revenue: ₹{total_revenue:,.2f}")

# -------------------------------
# 2. Average Sales
# -------------------------------
average_sales = df[sales_column].mean()
print(f"📊 Average Sales: ₹{average_sales:,.2f}")

# -------------------------------
# 3. Highest & Lowest Sale
# -------------------------------
max_sale = df[sales_column].max()
min_sale = df[sales_column].min()

print(f"📈 Highest Sale: ₹{max_sale:,.2f}")
print(f"📉 Lowest Sale: ₹{min_sale:,.2f}")

# -------------------------------
# 4. Best Selling Product
# -------------------------------
product_sales = df.groupby(product_column)[sales_column].sum()

best_product = product_sales.idxmax()
best_product_sales = product_sales.max()

print(f"🏆 Best Selling Product: {best_product}")
print(f"💵 Sales of Best Product: ₹{best_product_sales:,.2f}")

# -------------------------------
# 5. Top 5 Products
# -------------------------------
top_products = product_sales.sort_values(ascending=False).head(5)

print("\n🔥 Top 5 Products:\n")
print(top_products)

# -------------------------------
# 6. Sales Summary by Product
# -------------------------------
print("\n📊 Sales Summary by Product:\n")
print(product_sales)

# -------------------------------
# 7. Optional: Save Analysis
# -------------------------------
product_sales.to_csv("product_sales_summary.csv")

print("\n💾 Product-wise summary saved as product_sales_summary.csv")

print("\n✅ Day 4 Completed!")