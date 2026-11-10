import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_theme(style="whitegrid")

# Load data
df = pd.read_csv("Retail_Sales_Data_Unlox (1).csv")
df['Date'] = pd.to_datetime(df['Date'])
df['Year_Month'] = df['Date'].dt.to_period('M').astype(str)

# 1. Monthly Revenue Trend Chart
plt.figure(figsize=(12, 6))
monthly_rev = df.groupby('Year_Month')['Revenue'].sum().reset_index()
sns.lineplot(data=monthly_rev, x='Year_Month', y='Revenue', marker='o', color='#1f77b4', linewidth=2.5)
plt.title('Monthly Revenue Trend (2023 - 2024)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Year-Month', fontsize=11)
plt.ylabel('Total Revenue (₹)', fontsize=11)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('monthly_revenue_trend.png', dpi=300)
plt.close()

# 2. Revenue by Product Category Chart
plt.figure(figsize=(10, 6))
cat_rev = df.groupby('Product_Category')['Revenue'].sum().sort_values(ascending=True).reset_index()
sns.barplot(data=cat_rev, x='Revenue', y='Product_Category', palette='crest')
plt.title('Total Revenue by Product Category', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Revenue (₹)', fontsize=11)
plt.ylabel('Product Category', fontsize=11)
plt.tight_layout()
plt.savefig('category_revenue.png', dpi=300)
plt.close()

print("Visualizations saved successfully as PNG files!")