# ==========================================
# Day 5: Create Report
# ==========================================

import pandas as pd

# Load cleaned dataset
df = pd.read_csv("cleaned_sales_data.csv")  # or your file name

print("📝 Day 5: Creating Report...\n")

# -------------------------------
# Column Names (EDIT if needed)
# -------------------------------
sales_column = "Total_Sales"
product_column = "Product"

# -------------------------------
# Calculate Metrics
# -------------------------------
total_revenue = df[sales_column].sum()
average_sales = df[sales_column].mean()
max_sale = df[sales_column].max()
min_sale = df[sales_column].min()

product_sales = df.groupby(product_column)[sales_column].sum()
best_product = product_sales.idxmax()

# -------------------------------
# Generate Report Text
# -------------------------------
report = f"""
Sales Analysis Report
=====================

📊 Key Metrics:
- Total Revenue: ₹{total_revenue:,.2f}
- Average Sales: ₹{average_sales:,.2f}
- Highest Sale: ₹{max_sale:,.2f}
- Lowest Sale: ₹{min_sale:,.2f}
- Best Selling Product: {best_product}

🔥 Top 5 Products:
{product_sales.sort_values(ascending=False).head(5)}

💡 Insights:
- High-performing products contribute most to revenue
- Data was cleaned (missing values + duplicates removed)
- Focus on top-selling products to increase profit

"""

# -------------------------------
# Save Report
# -------------------------------
with open("analysis_report.txt", "w") as f:
    f.write(report)

print(report)

print("✅ Report saved as analysis_report.txt")
print("\n🎉 Day 5 Completed!")