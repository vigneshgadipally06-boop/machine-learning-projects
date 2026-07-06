import pandas as pd

def preprocess(df):
    df = pd.get_dummies(df, drop_first=True)
    df = df.fillna(df.mean(numeric_only=True))
    return df