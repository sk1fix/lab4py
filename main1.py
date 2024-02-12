import pandas as pd
import matplotlib.pyplot as pt


def read_csv(path: str) -> pd.DataFrame:
    df=pd.read_csv(path)
    df.columns=['Date', 'Course']
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
    df = df.dropna()
    df_mean = df["Value"].mean()
    df_median = df["Value"].median()
    df["Mean"] = df.apply(lambda x: (abs(x["Value"] - df_mean)), axis=1)
    df["Median"] = df.apply(lambda x: (abs(x["Value"] - df_median)), axis=1)
    df = df.sort_values(by="Date", ascending=True)
    return df