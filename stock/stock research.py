import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Function to fetch stock data
def fetch_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

# Feature engineering
def add_features(data):
    data['SMA_20'] = data['Close'].rolling(window=20).mean()
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    data['Volatility'] = data['Close'].rolling(window=20).std()
    data['Momentum'] = data['Close'] / data['Close'].shift(5) - 1
    data['Daily_Return'] = data['Close'].pct_change()
    data = data.dropna()
    return data

# Prepare dataset for training
def prepare_dataset(data):
    features = ['SMA_20', 'SMA_50', 'Volatility', 'Momentum', 'Daily_Return']
    X = data[features]
    y = data['Close']
    return X, y

# Train a model
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    print(f"Model RMSE: {rmse}")
    return model, X_test, y_test

# Predict future stock prices
def predict_future(model, latest_data):
    prediction = model.predict([latest_data])
    return prediction[0]

# Visualization
def plot_stock_data(stock_data, predictions=None):
    plt.figure(figsize=(12, 6))
    plt.plot(stock_data['Close'], label='Actual Prices', color='blue')
    if predictions is not None:
        plt.plot(predictions.index, predictions, label='Predicted Prices', color='orange')
    plt.title('Stock Price Prediction')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    ticker = input("Enter stock ticker symbol (e.g., AAPL): ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    # Fetch and process data
    stock_data = fetch_stock_data(ticker, start_date, end_date)
    stock_data = add_features(stock_data)

    # Prepare dataset and train model
    X, y = prepare_dataset(stock_data)
    model, X_test, y_test = train_model(X, y)

    # Predict future price
    latest_data = X.iloc[-1].values
    future_price = predict_future(model, latest_data)
    print(f"Predicted future price: {future_price}")

    # Plot actual and predicted prices
    plot_stock_data(stock_data)
