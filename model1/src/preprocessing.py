import numpy as np
import pandas as pd

def remove_outliers(train_df):
    return train_df.drop(train_df[(train_df['GrLivArea'] > 4000) & (train_df['SalePrice'] < 300000)].index)

def log_transform_target(train_df):
    train_df['SalePrice'] = np.log1p(train_df['SalePrice'])
    return train_df

def basic_cleaning(train_df, test_df):
    # Drop these columns
    cols_to_drop = ['PoolQC', 'MiscFeature', 'Alley', 'Fence', 'FireplaceQu']
    train_df = train_df.drop(columns=cols_to_drop, errors='ignore')
    test_df = test_df.drop(columns=cols_to_drop, errors='ignore')

    # Combine to impute consistently
    y = train_df['SalePrice']
    train_df.drop(['SalePrice'], axis=1, inplace=True)
    all_data = pd.concat([train_df, test_df], sort=False)

    # Fill LotFrontage with median per neighborhood
    all_data['LotFrontage'] = all_data.groupby('Neighborhood')['LotFrontage'].transform(lambda x: x.fillna(x.median()))

    # Fill categorical NAs with 'None'
    for col in ['GarageType', 'GarageFinish', 'GarageQual', 'GarageCond',
                'BsmtFinType1', 'BsmtFinType2', 'BsmtCond', 'BsmtExposure', 'BsmtQual',
                'MasVnrType', 'MSZoning', 'Utilities', 'Functional']:
        all_data[col] = all_data[col].fillna('None')

    # Fill numeric NAs with 0 or mode
    num_fill_zero = ['GarageYrBlt', 'GarageArea', 'GarageCars', 'BsmtFinSF1',
                     'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'BsmtFullBath', 'BsmtHalfBath', 'MasVnrArea']
    for col in num_fill_zero:
        all_data[col] = all_data[col].fillna(0)

    for col in ['MSZoning', 'Electrical', 'KitchenQual', 'Exterior1st', 'Exterior2nd', 'SaleType']:
        all_data[col] = all_data[col].fillna(all_data[col].mode()[0])

    # Convert MSSubClass to categorical
    all_data['MSSubClass'] = all_data['MSSubClass'].astype(str)

    # Add back target and return
    n_train = train_df.shape[0]
    train_cleaned = all_data.iloc[:n_train, :].copy()
    test_cleaned = all_data.iloc[n_train:, :].copy()
    train_cleaned['SalePrice'] = y

    return train_cleaned, test_cleaned
