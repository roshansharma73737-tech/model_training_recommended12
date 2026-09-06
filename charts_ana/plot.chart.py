import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Step 1: Load the CSV into a DataFrame
dataset_path = Path(__file__).resolve().parent.parent / 'data' / 'dataset.csv'

df = pd.read_csv(dataset_path)  


user_average = df.groupby('User_ID')['Rating'].mean().reset_index()


# line ploting 
plt.figure(figure =(10,5))
plt.plot(user_average['User_ID'][:50],user_average['Rating'][:50], mark = 'o')
plt.titl()