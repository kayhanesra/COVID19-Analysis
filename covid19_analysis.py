# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#I had the issue with version, check it for next reference //
import seaborn as sns
from matplotlib import rcParams

# Ensure matplotlib uses a compatible backend
plt.switch_backend('TkAgg')  # Use 'TkAgg' for GUI support or 'Agg' for headless environments

# Load the COVID-19 dataset
data_path = 'C:/Users/esrak/Desktop/COVID19-Analysis/covid_19_clean_complete.csv'
try:
    data = pd.read_csv(data_path)
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print(f"Error: File not found at {data_path}")
    exit()

# Display the first few rows of the dataset
print("Dataset Preview:")
print(data.head())

# Data Cleaning
data.dropna(subset=['Date', 'Country/Region', 'Confirmed', 'Deaths', 'Recovered'], inplace=True)
data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')
data['Active'] = data['Confirmed'] - data['Deaths'] - data['Recovered']

# Visualization: Top 10 countries by confirmed cases
country_summary = data.groupby('Country/Region')['Confirmed'].max().sort_values(ascending=False).head(10)

# Convert to DataFrame for plotting
country_summary_df = country_summary.reset_index()
country_summary_df.columns = ['Country/Region', 'Confirmed']
# Plots will show how the charts will be shown
# First Plot: Top 10 countries by confirmed cases// US to Iran//
plt.figure(figsize=(10, 6))
sns.barplot(
    x=country_summary_df['Confirmed'],
    y=country_summary_df['Country/Region'],
    palette='coolwarm'
)
plt.title('Top 10 Countries by Confirmed COVID-19 Cases')
plt.xlabel('Total Confirmed Cases')
plt.ylabel('Country/Region')
plt.savefig('top_10_countries.png', dpi=300, bbox_inches='tight')
plt.show()

# Visualization: Top 10 countries by deaths
death_summary = data.groupby('Country/Region')['Deaths'].max().sort_values(ascending=False).head(10)

# Convert to DataFrame for plotting
death_summary_df = death_summary.reset_index()
death_summary_df.columns = ['Country/Region', 'Deaths']

# Second Plot: Top 10 countries by deaths// will shown as brick color
plt.figure(figsize=(10, 6))
sns.barplot(
    x=death_summary_df['Deaths'],
    y=death_summary_df['Country/Region'],
    palette='Reds'
)
plt.title('Top 10 Countries by COVID-19 Deaths')
plt.xlabel('Total Deaths')
plt.ylabel('Country/Region')
plt.savefig('top_10_deaths.png', dpi=300, bbox_inches='tight')
plt.show()

# Visualization: Top 10 countries by recoveries
recovery_summary = data.groupby('Country/Region')['Recovered'].max().sort_values(ascending=False).head(10)

# Convert to DataFrame for plotting
recovery_summary_df = recovery_summary.reset_index()
recovery_summary_df.columns = ['Country/Region', 'Recovered']

# Third Plot: Top 10 countries by recoveries//will shown green
plt.figure(figsize=(10, 6))
sns.barplot(
    x=recovery_summary_df['Recovered'],
    y=recovery_summary_df['Country/Region'],
    palette='Greens'
)
plt.title('Top 10 Countries by COVID-19 Recoveries')
plt.xlabel('Total Recoveries')
plt.ylabel('Country/Region')
plt.savefig('top_10_recoveries.png', dpi=300, bbox_inches='tight')
plt.show()
