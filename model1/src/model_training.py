# src/model_training.py

from xgboost import XGBRegressor
import joblib

def train_xgb_model(X_train, y_train, model_path="models/xgb_model.pkl"):
    model = XGBRegressor(n_estimators=1000, learning_rate=0.05)
    model.fit(X_train, y_train)
    joblib.dump(model, model_path)
    return model
