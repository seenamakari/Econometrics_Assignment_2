import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.stattools import acf
from statsmodels.tsa.stattools import pacf

# Load the dataset into a DataFrame
df = pd.read_csv('Stocks.csv')

# Calculating simple returns from one row to the next
df['Simple_Returns'] = df['Close'].pct_change()
df = df.dropna(subset=['Simple_Returns'])

df['Log_Returns'] = np.log(df['Close']) - np.log(df['Close'].shift(1))
df = df.dropna(subset=['Log_Returns'])

simple_returns_column = df['Simple_Returns']

print("The following is ACF")
simple_returns_acf = acf(simple_returns_column, nlags=10)
print(simple_returns_acf)

print("The following is PACF")
pacf_values = pacf(simple_returns_column, nlags=10)
print(pacf_values)


