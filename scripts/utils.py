# Utility script for reusable functions

def load_and_process_data(file_path):
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df.sort_index(inplace=True)
    df.fillna(method='ffill', inplace=True)
    return df
