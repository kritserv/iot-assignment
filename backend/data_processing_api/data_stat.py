import pandas as pd

def get_statistics(df):
    result = {}
    for column in ('temperature', 'humidity', 'air_quality'):
        result[column] = {
            'mean': df[column].mean(),
            'median': df[column].median(),
            'min': df[column].min(),
            'max': df[column].max()
        }
    return result
