import pandas as pd
import numpy as np

# Changed dataset into a DataFrame
df = pd.read_csv('WE.csv')

# Set the date column as the index
df.set_index('Date', inplace=True)

#Adding the column for simple daily returns
df['simple_daily_return'] = (df['Close'] / df['Open']) - 1

print(df)