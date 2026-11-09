import pandas as pd

def validate_dataframe(df):
    return pd.DataFrame({
        "data_type": df.dtypes.astype(str),
        "missing_values": df.isna().sum(),
        "missing_percent": (df.isna().mean() * 100).round(2),
        "unique_values": df.nunique()
    })
