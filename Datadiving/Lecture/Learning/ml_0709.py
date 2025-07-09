# iris 파일 불러오기

import pandas as pd
import numpy as np

df = pd.read_csv("./csv_data/iris.csv")

print(df.head())
print(df.columns)
print(df.describe())
print(df.info())