#%%
import pandas as pd
import numpy as np

import torch
import torch.nn as nn

from torch.utils.data import Dataset
#%%
class LottoDataset(Dataset) : 
    def __init__(self,x_samples,y_samples,idx_range):        
        self.x_sample = x_samples[idx_range[0]:idx_range[1]]
        self.y_sample = y_samples[idx_range[0]:idx_range[1]]
    
    def __len__(self) : 
        return len(self.x_sample)
    
    def __getitem__(self, index):
        x = torch.tensor(self.x_sample[index],dtype=torch.float32)
        y = torch.tensor(self.y_sample[index],dtype=torch.float32)
        return x,y
#%% 원핫 인코딩 함수
def number2ohbin(numbers) :
    ohbin = np.zeros(45)
    for num in numbers:
        ohbin[int(num)-1] = 1
    return ohbin

def ohbin2numbers(ohbin) :
    numbers = [i+1 for i in range(len(ohbin)) if ohbin[i] == 1.0]
    return numbers
            
# %%
#numbers = ohbin2numbers([1.0,0.0,0.0,1.0,0.0])
#print(numbers)
#%%
#numbers = [3,41,17,2,9]
#print(number2ohbin(numbers))

# %% load data
data_1 = pd.read_csv('../__datasets__/lotto_1.csv')
data_2 = pd.read_csv('../__datasets__/lotto_2.csv')

data = pd.concat([data_1,data_2],ignore_index=True)
lotto_numbers = data[['c1','c2','c3','c4','c5','c6','cb']].values
#lotto_numbers.head()
# %%
ohbins = list(map(number2ohbin,lotto_numbers))
#print(ohbins)

#%%
seq_length = 5
x_sample = [ohbins[i:(i+seq_length)] for i in range(len(ohbins) - seq_length ) ]
y_sample = ohbins[seq_length:]

#%%
#print(x_sample[0])
#print(y_sample[0])

print(f'total samples : {len(x_sample)}')
total_samples = len(x_sample)

train_idx = (0,int(total_samples * 0.8))
test_idx = (int(total_samples * 0.8),int(total_samples * 0.9))
val_idx = (int(total_samples * 0.9),int(total_samples))

print(f" tran : {train_idx} , test : {test_idx} , val : {val_idx}")
# %% dataset create
train_dataset = LottoDataset(x_sample,y_sample,train_idx)
test_dataset = LottoDataset(x_sample,y_sample,test_idx)
val_dataset = LottoDataset(x_sample,y_sample,val_idx)

def getLottoDataset() :
    return train_dataset,test_dataset,val_dataset
