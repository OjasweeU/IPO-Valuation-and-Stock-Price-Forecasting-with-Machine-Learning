import pandas as pd
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
import numpy as np
import matplotlib.pyplot as plt

# Load processed data
tata_tech = pd.read_csv('TATA TECH_processed.csv', index_col='Date', parse_dates=True)

# Feature Selection
X = tata_tech[['Close_Scaled', 'MA20_Scaled']]
y = tata_tech['Close']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Support Vector Regression
svr = SVR(kernel='rbf')
svr.fit(X_train, y_train)
y_pred_svr = svr.predict(X_test)
print("SVR RMSE:", mean_squared_error(y_test, y_pred_svr, squared=False))

# Random Forest
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
print("Random Forest RMSE:", mean_squared_error(y_test, y_pred_rf, squared=False))

# LSTM
X_lstm_train = np.reshape(X_train.values, (X_train.shape[0], 1, X_train.shape[1]))
X_lstm_test = np.reshape(X_test.values, (X_test.shape[0], 1, X_test.shape[1]))

model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(1, X_lstm_train.shape[2])))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=False))
model.add(Dropout(0.2))
model.add(Dense(units=1))

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_lstm_train, y_train, epochs=20, batch_size=32)

y_pred_lstm = model.predict(X_lstm_test)
print("LSTM RMSE:", mean_squared_error(y_test, y_pred_lstm, squared=False))
