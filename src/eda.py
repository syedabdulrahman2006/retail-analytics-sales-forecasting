import pandas as pd

df = pd.read_csv("Retail_Sales_Data_Unlox (1).csv")

print("--- 1. DATASET SHAPE ---")
print(df.shape)

print("\n--- 2. OVERALL METRICS ---")
total_revenue = df['Revenue'].sum()
total_units = df['Units_Sold'].sum()
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Total Units Sold: {total_units:,}")

print("\n--- 3. TOP REVENUE BY PRODUCT CATEGORY ---")
category_sales = df.groupby('Product_Category')['Revenue'].sum().sort_values(ascending=False)
print(category_sales)

print("\n--- 4. TOP REGIONS BY REVENUE ---")
region_sales = df.groupby('Region')['Revenue'].sum().sort_values(ascending=False)
print(region_sales)
