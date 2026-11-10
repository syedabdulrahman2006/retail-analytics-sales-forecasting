import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Load data and prepare monthly revenue series
df = pd.read_csv("Retail_Sales_Data_Unlox (1).csv")
df['Date'] = pd.to_datetime(df['Date'])
df['Year_Month'] = df['Date'].dt.to_period('M')

# Group by month and sum revenue
monthly_sales = df.groupby('Year_Month')['Revenue'].sum().reset_index()
monthly_sales['Year_Month'] = monthly_sales['Year_Month'].dt.to_timestamp()
monthly_sales.set_index('Year_Month', inplace=True)

print("--- Historical Monthly Revenue Summary ---")
print(monthly_sales.head())

# Fit a simple ARIMA model (p, d, q)
# Data spans 2023-2024 (24 months)
model = ARIMA(monthly_sales['Revenue'], order=(1, 1, 1))
model_fit = model.fit()

print("\n--- ARIMA Model Summary ---")
print(model_fit.summary().tables[1])

# Forecast the next 3 months (e.g., early 2025)
forecast_steps = 3
forecast = model_fit.forecast(steps=forecast_steps)

print(f"\n--- Revenue Forecast for Next {forecast_steps} Months ---")
print(forecast)