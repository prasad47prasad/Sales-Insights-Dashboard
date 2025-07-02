# 📦 Enhanced Sales Data Analysis Project with Extra Features

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the file
df = pd.read_csv("sales_data.csv")

# Step 2: Clean column names
df.columns = df.columns.str.strip()

# Step 3: Drop null rows
df = df.dropna()

# Step 4: Convert to numeric safely
df['Quantity Ordered'] = pd.to_numeric(df['Quantity Ordered'], errors='coerce')
df['UnitPrice'] = pd.to_numeric(df['UnitPrice'], errors='coerce')
df = df.dropna()

# Step 5: Convert OrderDate to datetime
df['OrderDate'] = pd.to_datetime(df['OrderDate'], errors='coerce')
df = df.dropna(subset=['OrderDate'])

# Step 6: Extract Month, Year, Month-Year
df['Month'] = df['OrderDate'].dt.month
df['Year'] = df['OrderDate'].dt.year
df['Month-Year'] = df['OrderDate'].dt.to_period('M')

# Step 7: Create Total column
df['Total'] = df['Quantity Ordered'] * df['UnitPrice']

# ✅ Feature 1: Monthly Sales
monthly_sales = df.groupby('Month')['Total'].sum()
print("Monthly Sales:\n", monthly_sales)
monthly_sales.plot(kind='bar', figsize=(10, 5), title="Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales in ₹")
plt.grid()
plt.show()

# ✅ Feature 2: Top 5 Products
top_products = df.groupby('Product')['Total'].sum().sort_values(ascending=False).head(5)
print("Top 5 Products:\n", top_products)
top_products.plot(kind='bar', title='Top 5 Products by Sales', figsize=(10, 5))
plt.ylabel("Sales in ₹")
plt.grid()
plt.show()

# ✅ Feature 3: Sales Trend Over Time
trend = df.groupby('Month-Year')['Total'].sum()
trend.plot(kind='line', marker='o', title='Monthly Sales Trend Over Time', figsize=(12, 6))
plt.ylabel('Sales in ₹')
plt.grid()
plt.show()

# ✅ Feature 4: Best Month for Sales
best_month = monthly_sales.idxmax()
max_value = monthly_sales.max()
print(f"\n📈 Best Month for Sales: Month {best_month} with ₹{max_value:.2f}")

# ✅ EXTRA Feature 1: Most Ordered Products by Quantity
most_ordered = df.groupby('Product')['Quantity Ordered'].sum().sort_values(ascending=False).head(5)
print("Most Ordered Products:\n", most_ordered)
most_ordered.plot(kind='bar', title='Most Ordered Products by Quantity', figsize=(10,5))
plt.ylabel('Quantity')
plt.grid()
plt.show()

# ✅ EXTRA Feature 2: Hourly Sales Trend (if OrderDate has time)
df['Hour'] = df['OrderDate'].dt.hour
hourly_sales = df.groupby('Hour')['Total'].sum()
hourly_sales.plot(kind='line', marker='o', title='Sales by Hour', figsize=(10,5))
plt.xlabel('Hour of Day')
plt.ylabel('Sales in ₹')
plt.grid()
plt.show()

# ✅ Optional: Save plots (Uncomment to use)
# plt.savefig("monthly_sales.png")
# plt.savefig("top_products.png")
# plt.savefig("sales_trend.png")
# plt.savefig("most_ordered.png")
# plt.savefig("hourly_sales.png")