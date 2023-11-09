import pandas as pd
import numpy as np

# Changed dataset into a DataFrame
df = pd.read_csv('Stocks.csv')

# Calculate simple returns from one row to the next
df['Simple_Returns'] = df['Close'].pct_change()

# Drop rows with NaN values (which will be the first row after calculating returns)
df = df.dropna(subset=['Simple_Returns'])

df['simple_return'] = (df['Close'] / df['Close'].shift(1)) - 1
