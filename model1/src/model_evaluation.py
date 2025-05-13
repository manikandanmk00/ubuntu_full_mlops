# src/model_evaluation.py

import joblib
from sklearn.metrics import mean_squared_error
import numpy as np

def evaluate_model(X, y_true, model_path="models/xgb_model.pkl"):
    model = joblib.load(model_path)
    y_pred = model.predict(X)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    return rmse
