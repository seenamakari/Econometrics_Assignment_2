import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.api import VAR
import matplotlib.pyplot as plt

# Load the dataset into a DataFrame
df = pd.read_csv('Canada.csv')

df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

print(results.summary())




