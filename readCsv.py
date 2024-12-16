import pandas as pd
import numpy as py

# using padas
data=pd.read_csv("data.csv")
print(data)

# using numpy
data1=py.genfromtxt('data.csv',delimiter=',',dtype=None, encoding="utf-8", skip_header=1)
print(data1)