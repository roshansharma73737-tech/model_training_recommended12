import pandas as pd
import numpy as np

df = pd.read_csv('../data/dataset.csv')
print("first  5 rowa ",df.head())
print("last 5 rows", df.tail())
print("\ncolumn  infomation ")
df.info()

print("\n this stastistical summary of the dataset:\n", df.describe())


rating_array = df['rating'].to.numpy()
print("\nmean rating of the dataset is ", np.mean(rating_array))
print("\n standard deviation of the rating is ", np.std(rating_array))
print("\n Unique user",np.unique(df['userId']).size)
