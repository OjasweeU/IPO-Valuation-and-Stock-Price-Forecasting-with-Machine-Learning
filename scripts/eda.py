import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mplfinance as mpf

# Load processed data
tata_tech = pd.read_csv('TATA TECH_processed.csv', index_col='Date', parse_dates=True)
tech_mahindra = pd.read_csv('TECHM_processed.csv', index_col='Date', parse_dates=True)
infosys = pd.read_csv('INFY_processed.csv', index_col='Date', parse_dates=True)
wipro = pd.read_csv('WIPRO_processed.csv', index_col='Date', parse_dates=True)
hcl_tech = pd.read_csv('HCLTECH_processed.csv', index_col='Date', parse_dates=True)

# Plot candlestick charts with moving averages
for name, df in [('TATA TECH', tata_tech), ('TECHM', tech_mahindra), ('INFY', infosys), ('WIPRO', wipro), ('HCLTECH', hcl_tech)]:
    moving_averages = [mpf.make_addplot(df['MA20'], color='blue', label='MA 20'),
                       mpf.make_addplot(df['MA50'], color='red', label='MA 50')]
    
    mpf.plot(df, type='candle', title=f'{name} Stock Price with Moving Averages',
             style='charles', addplot=moving_averages, volume=True)
    plt.show()

# Correlation Analysis
correlation_matrix = tata_tech.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix for Tata Technologies")
plt.show()
