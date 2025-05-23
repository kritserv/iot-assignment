import pandas as pd

def remove_duplicated(df):
    return df.drop_duplicates(subset=['timestamp'])

def fix_missing_values(df):
    df = df.set_index('timestamp')
    numeric_columns = df.select_dtypes(include=['number']).columns
    df[numeric_columns] = df[numeric_columns].interpolate(method='time')
    return df.reset_index()

def detect_outliers(df):
    df = df.copy()
    for col in ('temperature', 'humidity', 'air_quality'):
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        df[f"{col}_outlier"] = (df[col] < lower) | (df[col] > upper)

    return df
