import pandas as pd


def preprocess(data_path, format='csv'):
    if format == 'csv':
        melbourne_data = pd.read_csv(data_path)
    elif format == 'json':
        melbourne_data = pd.read_json(data_path)

    # dropna drops missing values (think of na as "not available")
    melbourne_data = melbourne_data.dropna(axis=0)
    return melbourne_data