import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Step 1: Load the CSV into a DataFrame
dataset_path = Path(__file__).resolve().parent.parent / 'data' / 'dataset.csv'

df = pd.read_csv(dataset_path)  


user_average = df.groupby('User_ID')['Rating'].mean().reset_index()


# line ploting 
plt.figure(figsize =(10,5))
plt.plot(user_average['User_ID'][:50],user_average['Rating'][:50], marker = 'o')
plt.title('Average RAting per user (first  10 users )')
plt.xlabel('user id ')
plt.ylabel('Average rating  ')
plt.grid(True)
plt.savefig('rating_trend.png')
plt.show()


# step  3 --> Analyze the  whatls charts shows ->
print( "highest  avrg  rating user:\n",user_average.loc[user_average['Rating'].idxmax()])
print("\nlowest aveerage rating user:\n",user_average.loc[user_average['Rating'].idxmin()])
print("\n Overall average rating across all users:", user_average['Rating'].mean())
