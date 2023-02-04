import pandas as pd

df = pd.read_sas('./LLCP2021.XPT', index=None)

df.to_csv('./LLCP2021.csv')
