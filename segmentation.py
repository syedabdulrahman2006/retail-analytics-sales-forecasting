import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_csv("Retail_Sales_Data_Unlox (1).csv")

# Aggregate performance metrics per store
store_metrics = df.groupby('Store_ID').agg(
    Total_Revenue=('Revenue', 'sum'),
    Total_Units=('Units_Sold', 'sum'),
    Avg_Rating=('Store_Rating', 'mean'),
    Transaction_Count=('Date', 'count')
).reset_index()

print("--- Store Metrics Preview ---")
print(store_metrics.head())

# Prepare features for clustering
X = store_metrics[['Total_Revenue', 'Total_Units', 'Avg_Rating', 'Transaction_Count']]

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply K-Means clustering (let's use 3 clusters: High, Medium, Low performance)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
store_metrics['Cluster'] = kmeans.fit_predict(X_scaled)

# Map clusters to descriptive labels based on average revenue
cluster_summary = store_metrics.groupby('Cluster')['Total_Revenue'].mean().sort_values().index
label_map = {cluster_summary[0]: 'Low-Performing', cluster_summary[1]: 'Medium-Performing', cluster_summary[2]: 'High-Performing'}
store_metrics['Performance_Segment'] = store_metrics['Cluster'].map(label_map)

print("\n--- Store Segments Summary ---")
print(store_metrics['Performance_Segment'].value_counts())

print("\n--- Sample Segmented Stores ---")
print(store_metrics[['Store_ID', 'Total_Revenue', 'Performance_Segment']].head(10))

# Save output to a CSV for your dashboard or report
store_metrics.to_csv("store_segments.csv", index=False)
print("\nStore segments saved to 'store_segments.csv'!")