import pandas as pd

df = pd.read_csv('hh.csv')
print(df[df['зарплата'] > 100000])

