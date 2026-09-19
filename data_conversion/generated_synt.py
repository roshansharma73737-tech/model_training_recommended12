import  numpy as np 
import  pandas as pd
import os 


os.makedirs('../data', exist_ok= True)

np.random.seed(42)

data =pd.DataFrame({
    'user_id': np.random.randint(1,101,2000),
    'rating': np.random.randint(1,6,2000),
    'item_id': np.random.randint(1,51,2000),

})


data = data.drop_duplicates(
    subset=['user_id','item_id']
)
data.to_csv('../data/rating.csv', index= False)
print("synthetic data  created at ../data/rating.csv")
print("The  synthetic data printed successfully ! ")
print(data.head())