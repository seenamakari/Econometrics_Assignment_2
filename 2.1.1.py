import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.api import VAR
import matplotlib.pyplot as plt

# Load the dataset into a DataFrame
df = pd.read_csv('Question_2.csv')

df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Plotting M2++ (gross)
df['M2++ (gross)'].plot()
plt.title('M2++ (gross)')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()


# Plotting CPI
df['CPI)'].plot()
plt.title('CPI')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()


# Plotting Bank Rate
df['Bank Rate'].plot()
plt.title('Bank Rate')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()


model = VAR(df)
results = model.fit(1)  # Fit a VAR(1) model
print(results.summary())
















