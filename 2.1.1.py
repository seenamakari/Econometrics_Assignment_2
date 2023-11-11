import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.api import VAR
import matplotlib.pyplot as plt

# Load the dataset into a DataFrame
df = pd.read_csv('Question_2.csv')

df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Plotting Bank Rate
df['Bank Rate'].plot()
plt.title('Bank Rate')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()







