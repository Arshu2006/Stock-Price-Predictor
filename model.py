import yfinance as yf
import numpy as np

def predict_stock(symbol):

    data = yf.download(
        symbol,
        period="6mo"
    )

    close_prices = data["Close"].values

    # Simple prediction using average of last 5 days
    prediction = np.mean(
        close_prices[-5:]
    )

    return round(float(prediction),2)