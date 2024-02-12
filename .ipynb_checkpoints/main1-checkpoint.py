import pandas as pd
import matplotlib.pyplot as pt


def read_csv(path: str) -> pd.DataFrame:
    df=pd.read_csv(path)
    df.columns=['Date', 'Course']