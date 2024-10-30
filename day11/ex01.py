#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
#%%

data_1 = pd.read_csv('lotto_1.csv') # 1-600
data_2 = pd.read_csv('lotto_2.csv') # 601 ~

data = pd.concat([data_1,data_2],ignore_index=True)

#%%
data.info()


# %%
price_colums = ["win1_pric","win2_pric","win3_pric","win4_pric","win5_pric"]
for col in price_colums:
    print(f"conver colum {col}")
    data[col] = data[col].str.replace('원','').str.replace(',','').astype(np.int64)

data.info()

# %%
data.head()
# %%
plt.figure(figsize=[10,6])
data[['c1','c2','c3','c4','c5','c6','cb']].hist(bins=50)

plt.show()


# %%
colums = ['c1','c2','c3','c4','c5','c6']
recomandations ={}

for col in colums :
    most_common_number = data[col].value_counts().idxmax()
    recomandations[col] = most_common_number
print(recomandations)

# %%

def weighted_random_choice(column):
    value_count = data[column].value_counts()
    numbers = value_count.index.tolist()
    weights = value_count.values.tolist()
    
    chosen_number = random.choices(numbers,weights=weights,k=1)
    return chosen_number[0]

#%%
for col in colums:
    recomandations[col] = weighted_random_choice(col)

print("추천번호 : " , recomandations)

# %%
