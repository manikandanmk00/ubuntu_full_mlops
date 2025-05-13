from src.data_ingestion import load_raw_data
from src.preprocessing import remove_outliers, log_transform_target, basic_cleaning
from src.feature_engineering import engineer_features
from src.model_training import train_xgb_model
from src.model_evaluation import evaluate_model

def run_pipeline():
    train, test = load_raw_data("data/raw/train.csv", "data/raw/test.csv")

    train = remove_outliers(train)
    train = log_transform_target(train)
    train, test = basic_cleaning(train, test)

    X_train, X_test, y_train = engineer_features(train, test)

    train_xgb_model(X_train, y_train)
    rmse = evaluate_model(X_train, y_train)

    print(f"Training RMSE: {rmse:.4f}")

if __name__ == "__main__":
    run_pipeline()
