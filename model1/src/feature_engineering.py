# src/feature_engineering.py

import numpy as np
import pandas as pd
from scipy.stats import skew

def add_combined_features(df):
    df['TotalSF'] = df['TotalBsmtSF'] + df['1stFlrSF'] + df['2ndFlrSF']
    return df

def fix_skewness(df, numeric_feats=None):
    if numeric_feats is None:
        numeric_feats = df.dtypes[df.dtypes != "object"].index

    skewed_feats = df[numeric_feats].apply(lambda x: skew(x.dropna())).sort_values(ascending=False)
    skewed = skewed_feats[abs(skewed_feats) > 0.75].index
    df[skewed] = np.log1p(df[skewed])
    return df

def encode_categoricals(df):
    return pd.get_dummies(df)

def engineer_features(train_df, test_df):
    all_data = pd.concat([train_df.drop('SalePrice', axis=1), test_df], axis=0)

    all_data = add_combined_features(all_data)
    all_data = fix_skewness(all_data)
    all_data = encode_categoricals(all_data)

    X_train = all_data.iloc[:train_df.shape[0], :]
    X_test = all_data.iloc[train_df.shape[0]:, :]
    y_train = train_df['SalePrice']

    return X_train, X_test, y_train
