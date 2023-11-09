import pandas as pd
import numpy as np
import statsmodels.api as sm

# Load the dataset into a DataFrame
df = pd.read_csv('Stocks.csv')

# Calculating simple returns from one row to the next
df['Simple_Returns'] = df['Close'].pct_change()
df = df.dropna(subset=['Simple_Returns'])

df['Log_Returns'] = np.log(df['Close']) - np.log(df['Close'].shift(1))
df = df.dropna(subset=['Log_Returns'])

simple_returns_column = df['Simple_Returns']

# Fit an AutoReg(10) model
lags = 10  # Number of lags (AR terms)
model = sm.tsa.AutoReg(simple_returns_column, lags=lags)
results = model.fit()

print(results.summary())

#df_simple_returns = df[['Date', 'Simple_Returns']]
#df_simple_returns = df[['Date', 'Simple_Returns']]
#print(df_simple_returns)
#pd.plotting.lag_plot(df_simple_returns, lag=1)

