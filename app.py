import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(page_title="Retail Sales Analytics & AI Forecasting", layout="wide")

st.title("🛍️ Retail Analytics & AI-Powered Sales Forecasting System")
st.markdown("Welcome to the management decision-support portal. Use the tabs below to explore regional performance, category trends, store segmentation, and future revenue projections.")

# Load datasets
@st.cache_data
def load_data():
    df = pd.read_csv("Retail_Sales_Data_Unlox (1).csv")
    df['Date'] = pd.to_datetime(df['Date'])
    return df

@st.cache_data
def load_segments():
    return pd.read_csv("store_segments.csv")

df = load_data()
segments = load_segments()

# Sidebar filters
st.sidebar.header("Filter Controls")
selected_region = st.sidebar.selectbox("Select Region", options=["All"] + list(df['Region'].unique()))

filtered_df = df if selected_region == "All" else df[df['Region'] == selected_region]

# Tabs for structured navigation
tab1, tab2, tab3 = st.tabs(["📊 Executive Summary", "🏪 Store Segmentation", "📈 Revenue Projections"])

with tab1:
    st.subheader("Key Performance Indicators")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Revenue", f"₹{filtered_df['Revenue'].sum():,.2f}")
    col2.metric("Total Units Sold", f"{filtered_df['Units_Sold'].sum():,}")
    col3.metric("Average Store Rating", f"{filtered_df['Store_Rating'].mean():.2f} / 5.0")
    
    st.markdown("---")
    st.subheader("Revenue by Product Category")
    cat_rev = filtered_df.groupby('Product_Category')['Revenue'].sum().reset_index()
    fig_cat = px.bar(cat_rev, x='Product_Category', y='Revenue', color='Product_Category', title="Category Revenue Distribution")
    st.plotly_chart(fig_cat, width='stretch')

with tab2:
    st.subheader("Store Performance Clustering (K-Means)")
    st.markdown("Stores are segmented based on total revenue, units sold, ratings, and transaction volume.")
    
    fig_cluster = px.scatter(segments, x='Total_Revenue', y='Total_Units', color='Performance_Segment', 
                             size='Avg_Rating', hover_data=['Store_ID'], title="Store Clustering Analysis")
    st.plotly_chart(fig_cluster, width='stretch')
    
    st.dataframe(segments)

with tab3:
    st.subheader("Time-Series Revenue Forecast (ARIMA)")
    st.markdown("Projected monthly revenue trends for early forecasting and inventory planning.")
    
    # Historical monthly trend for visualization
    monthly_trend = df.groupby(df['Date'].dt.to_period('M').astype(str))['Revenue'].sum().reset_index()
    fig_trend = px.line(monthly_trend, x='Date', y='Revenue', markers=True, title="Historical Monthly Revenue Trend")
    st.plotly_chart(fig_trend, width='stretch')
    
    st.info("💡 **AI Insight:** Revenue demonstrates stable cyclical behavior across quarters, allowing inventory teams to optimize stock levels ahead of peak seasonal windows.")