import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load the CSV files
files = {
    'TATA TECH': 'TataTech One Yr data.csv',
    'TECHM': 'TechM One Yr data.csv',
    'INFY': 'Infosys one YR data.csv',
    'WIPRO': 'Wipro One Yr data.csv',
    'HCLTECH': 'HCLTech One Yr data.csv'
}

# Read the CSV files into DataFrames
data = {name: pd.read_csv(file) for name, file in files.items()}

# Process the data: Convert dates and set index
for name, df in data.items():
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df.sort_index(inplace=True)
    
    # Handle missing values
    df.fillna(method='ffill', inplace=True)

    # Feature Engineering
    df['MA20'] = df['Close'].rolling(window=20).mean()
    df['MA50'] = df['Close'].rolling(window=50).mean()
    df['Daily_Return'] = df['Close'].pct_change()
    df['Volatility'] = df['Daily_Return'].rolling(window=7).std()

    # Standardization
    scaler = MinMaxScaler()
    df[['Close_Scaled', 'MA20_Scaled']] = scaler.fit_transform(df[['Close', 'MA20']])

# Save the processed data
for name, df in data.items():
    df.to_csv(f'{name}_processed.csv')
