import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.stattools import acf
from statsmodels.tsa.stattools import pacf

# Load the dataset into a DataFrame
df = pd.read_csv('Question_1.csv')

# Calculating simple returns from one row to the next
df['Simple_Returns'] = df['Close'].pct_change()
df = df.dropna(subset=['Simple_Returns'])

df['Log_Returns'] = np.log(df['Close']) - np.log(df['Close'].shift(1))
df = df.dropna(subset=['Log_Returns'])

#Finding the ACF and PACF of simple returns
simple_returns_column = df['Simple_Returns']

print("The following is ACF for simple returns")
simple_returns_acf = acf(simple_returns_column, nlags=10)
print(simple_returns_acf)

print("The following is PACF for simple returns")
pacf_values = pacf(simple_returns_column, nlags=10)
print(pacf_values)

#Finding the ACF and PACF of log returns
log_returns_column = df['Log_Returns']

print("The following is ACF for log returns")
log_returns_acf = acf(log_returns_column, nlags=10)
print(log_returns_acf)

print("The following is PACF for log returns")
log_returns_pacf = pacf(log_returns_column, nlags=10)
print(log_returns_pacf)



