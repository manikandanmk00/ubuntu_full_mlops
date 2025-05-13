import pandas as pd
import os

def load_raw_data(train_path:str,test_path:str):
    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)
    return train,test