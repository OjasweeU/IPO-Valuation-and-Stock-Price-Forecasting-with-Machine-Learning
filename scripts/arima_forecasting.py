import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Load processed data
tata_tech = pd.read_csv('TATA TECH_processed.csv', index_col='Date', parse_dates=True)

# ARIMA Model
model = ARIMA(tata_tech['Close'], order=(5, 1, 0))
model_fit = model.fit()

forecast_object = model_fit.get_forecast(steps=30)
forecast = forecast_object.predicted_mean
conf_int = forecast_object.conf_int()

forecast_dates = pd.date_range(tata_tech.index[-1], periods=len(forecast), freq='D')

plt.figure(figsize=(10, 5))
plt.plot(tata_tech.index, tata_tech['Close'], label='Historical')
plt.plot(forecast_dates, forecast, label='Forecast')
plt.fill_between(forecast_dates, conf_int.iloc[:, 0], conf_int.iloc[:, 1], alpha=0.1)
plt.title('Stock Price Forecast with Confidence Intervals')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.show()
