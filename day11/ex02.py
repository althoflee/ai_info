#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn as nn

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

#%%

data_1 = pd.read_csv('lotto_1.csv') # 1-600
data_2 = pd.read_csv('lotto_2.csv') # 601 ~

data = pd.concat([data_1,data_2],ignore_index=True)

#%%
data.info()
# %%
data.set_index('iso',inplace=True)
data.sort_index(inplace=True)
data.head()
# %%

lotto_numbers = data[['c1','c2','c3','c4','c5','c6','cb']]
lotto_numbers.head()

# %%
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(lotto_numbers)


# %%
print(scaled_data)
print(scaled_data.shape)
# %%
def create_sequence(data,seqeunce_length) :
    sequences = []
    targets = []
    for i in range(len(data) - seqeunce_length) :
        seq = data[i: i+seqeunce_length]
        target = data[i+seqeunce_length]
        sequences.append(seq)
        targets.append(target)
    return np.array(sequences),np.array(targets)
#%%
sequence_length = 10

X,y = create_sequence(scaled_data,sequence_length)
#%%
print(X.shape)
print(y.shape)
# %%
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,shuffle=False)

X_train = torch.tensor(X_train,dtype=torch.float32)
y_train = torch.tensor(y_train,dtype=torch.float32)
X_test = torch.tensor(X_test,dtype=torch.float32)
y_test = torch.tensor(y_test,dtype=torch.float32)

#%%

print(X_train.shape)
print(X_test.shape)

print(y_train.shape)
print(y_test.shape)

# %%
