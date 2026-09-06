# 1_pandas_numpy_basics/load_and_read.py
import pandas as pd
import numpy as np
from pathlib import Path

# Step 1: Load the CSV into a DataFrame
dataset_path = Path(__file__).resolve().parent.parent / 'data' / 'dataset.csv'

df = pd.read_csv(dataset_path)

# Step 2: Read/explore with pandas
print("First 5 rows:\n", df.head())
print("\nColumn info:\n")
df.info()
print("\nStatistical summary:\n", df.describe())

# Step 3: Same data, using numpy directly (lower-level, faster for pure math)
ratings_array = df['Rating'].to_numpy()
print("\nMean rating (numpy):", np.mean(ratings_array))
print("Standard deviation:", np.std(ratings_array))
print("Total users:", np.unique(df['User_ID']).size)
