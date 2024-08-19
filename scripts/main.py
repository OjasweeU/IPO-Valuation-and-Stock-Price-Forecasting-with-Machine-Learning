# Main script to run the entire analysis pipeline

# Step 1: Data Processing
exec(open("data_processing.py").read())

# Step 2: Exploratory Data Analysis
exec(open("eda.py").read())

# Step 3: Modeling
exec(open("modeling.py").read())

# Step 4: ARIMA Forecasting
exec(open("arima_forecasting.py").read())

# Step 5: Results and Recommendations
# Add any final steps, conclusions, or recommendations based on the analysis
