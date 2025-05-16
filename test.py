import pandas as pd

df = pd.read_csv('var4.csv')
types = df.dtypes
print(type(types))