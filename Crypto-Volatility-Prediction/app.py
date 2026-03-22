import streamlit as st
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open(r"C:\Users\ASHUTOSH\Desktop\python\model.pkl", "rb"))
scaler = pickle.load(open(r"C:\Users\ASHUTOSH\Desktop\python\scaler.pkl", "rb"))
st.title("Crypto Volatility Predictor 🚀")

st.write("Enter cryptocurrency data:")

# Inputs
open_val = st.number_input("Open")
high = st.number_input("High")
low = st.number_input("Low")
close = st.number_input("Close")
volume = st.number_input("Volume")
market_cap = st.number_input("Market Cap")

if st.button("Predict"):

    # same feature engineering (IMPORTANT)
    vol_ratio = volume / (market_cap + 1)

    data = np.array([[open_val, high, low, close, volume, market_cap, close, close, vol_ratio]])

    # scale
    data = scaler.transform(data)

    # predict
    prediction = model.predict(data)

    st.success(f"Predicted Volatility: {prediction[0]}")
