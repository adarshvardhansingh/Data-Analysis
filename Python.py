import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('India_Key_Commodities_Retail_Prices_1997_2015.csv')

print(df.head())

print(df.describe())

# Removing any rows with missing values
df.dropna(inplace=True)

# Renaming the columns to be more descriptive
df.rename(columns={
    'Date': 'date',
    'Centre': 'centre',
    'Commodity': 'commodity',
    'Price per Kg': 'price_per_kg',
    'Region': 'region',
    'Country': 'country'
}, inplace=True)

# Converting the 'date' column to a datetime object
df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')

# Creating a new column to represent the month and year
df['month_year'] = df['date'].dt.to_period('M')

# Calculating the average price by month and year, commodity, and region
avg_prices = df.groupby(['month_year', 'commodity', 'region'])['price_per_kg'].mean().reset_index()

# Creating a pivot table to compare the average prices of different commodities and regions over time
pivot_table = pd.pivot_table(avg_prices, values='price_per_kg', index=['month_year'], columns=['commodity', 'region'])

# Creating a bar chart to show the total price of each commodity by region
plt.figure(figsize=(10, 6))
sns.barplot(x='commodity', y='price_per_kg', hue='region', data=df)
plt.title('Total Prices of Key Commodities in India by Region')
plt.xlabel('Commodity')
plt.ylabel('Price per Kg (INR)')
plt.xticks(rotation=45)
plt.show()

# Creating a scatter plot to show the relationship between price and date
plt.figure(figsize=(10, 6))
sns.scatterplot(x='date', y='price_per_kg', hue='commodity', data=df)
plt.title('Prices of Key Commodities in India over Time')
plt.xlabel('Date')
plt.ylabel('Price per Kg (INR)')
plt.xticks(rotation=45)
plt.show()

# Plotting the average price of each commodity by region as a scatter plot matrix
plt.figure(figsize=(10, 6))
sns.pairplot(data=avg_prices, hue='region')
plt.suptitle('Scatter Plot Matrix of Key Commodities in India by Region')
plt.show()

# Plotting the distribution of prices for each commodity and region as a violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(data=avg_prices, x='commodity', y='price_per_kg', hue='region')
plt.title('Distribution of Prices for Key Commodities in India by Region')
plt.show()