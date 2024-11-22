#%%
import torch
from torch.utils.data import Dataset,DataLoader

print('module load complete')
print(f'torch version : {torch.__version__}')

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f'device : {device}')

#%%
class MyXorDataset(Dataset) :
    def __init__(self,X,Y):
        self.x_data = X
        self.y_data = Y
        
    def __len__(self):
        return len(self.x_data)
    
    def __getitem__(self,idx):
        x = self.x_data[idx]
        y = self.y_data[idx]
        return x,y