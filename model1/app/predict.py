# app/predict.py
import joblib
import numpy as np
import pandas as pd

# Load your trained model (place it in models/xgb_model.pkl)
model = joblib.load("models/xgb_model.pkl")

def make_prediction(features: dict):
    df = pd.DataFrame([features])
    prediction = model.predict(df)
    return np.expm1(prediction[0])  # reverse log1p if you used log1p on SalePrice
