import pandas as pd
import numpy as np


def compute_concentration(df, category_col, value_col, time_col):
    result = []

    df[time_col] = pd.to_datetime(df[time_col])
    df['Year'] = df[time_col].dt.year

    for year, group in df.groupby('Year'):
        grouped = group.groupby(category_col)[value_col].sum().sort_values(ascending=False)
        total = grouped.sum()
        cumsum = grouped.cumsum() / total

        top_10 = grouped[cumsum <= 0.10]
        top_20 = grouped[cumsum <= 0.20]
        top_50 = grouped[cumsum <= 0.50]

        result.append({
            "Year": year,
            "Top 10%": top_10.sum(),
            "Top 20%": top_20.sum(),
            "Top 50%": top_50.sum(),
            "Total": total
        })

    return pd.DataFrame(result)



def detect_anomalies(df, value_col, z_thresh=2.0):
    import numpy as np

    df = df.copy()

    df[value_col] = pd.to_numeric(df[value_col], errors='coerce')
    df = df.dropna(subset=[value_col])

    mean = df[value_col].mean()
    std = df[value_col].std()

    if std == 0 or np.isnan(std):
        return pd.DataFrame()

    df['z_score'] = (df[value_col] - mean) / std

    print("Z-score debug:")
    print(df[[value_col, 'z_score']])

    return df[df['z_score'].abs() > z_thresh]
