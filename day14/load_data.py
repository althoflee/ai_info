#%%
import torch
from torch.utils.data import Dataset,DataLoader
from my_dataset import MyXorDataset

print('module load complete')
print(f'torch version : {torch.__version__}')

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f'device : {device}')

#%%
dataset = torch.load('xor_dataset.pth')
print(dataset)

#%%
dataloader = DataLoader(dataset,1,True)

for idx,(X,Y) in enumerate(dataloader) :
    print(X,Y)

# %%
