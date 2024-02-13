import pandas as pd
import matplotlib.pyplot as pt
from pandas import DataFrame
from datetime import date


def read_csv(path: str) -> DataFrame:
    df = pd.read_csv(path)
    df.columns = ['Date', 'Course']
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
    df = df.dropna()
    df_mean = df["Value"].mean()
    df_median = df["Value"].median()
    df["Mean"] = df.apply(lambda x: (abs(x["Value"] - df_mean)), axis=1)
    df["Median"] = df.apply(lambda x: (abs(x["Value"] - df_median)), axis=1)
    df = df.sort_values(by="Date", ascending=True)
    return df


def find_median_value(df: DataFrame, value: float) -> DataFrame:
    return df.query('Mean >= @value')


def find_delta_time_value(df: DataFrame, first: date, second: date) -> DataFrame:
    return df.query('Date >= @first and Date<=@second')


def sort_month(df: pd.DataFrame) -> pd.Series:
    return df.groupby(df.Date.dt.month)["Value"].mean()


def show_value_graph(df: pd.DataFrame) -> None:
    fig = pt.figure(figsize=(19, 5))
    pt.ylabel("Course")
    pt.xlabel("date")
    pt.title('Курс долара')
    pt.plot(df["Date"], df["Course"], color='blue',
            linestyle='-', linewidth=1)
    pt.show()


def course_per_month(df: DataFrame, date: date) -> None:
    p = df[(df["Date"].dt.year == date.year) &
           (df["Date"].dt.month == date.month)]
    p.plot(x="Date", y="Course", marker='o')
    pt.show()
