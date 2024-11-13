#%%
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset,DataLoader

from datautil import LottoDataset,getLottoDataset
#%%

batch_size = 64
train_data,test_data,val_data = getLottoDataset()

train_loader = DataLoader(train_data,64,shuffle=False)
test_loader = DataLoader(test_data,64,shuffle=False)
val_loader = DataLoader(val_data,64,shuffle=False)

#%%
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f'device : {device}')

class LottoPredictor(nn.Module) :
    def __init__(self):
        super(LottoPredictor,self).__init__()
        self.lstm = nn.LSTM(input_size=45,hidden_size=128,num_layers=1,batch_first=True)
        self.fc = nn.Linear(128,45)
        self.sigmoid = nn.Sigmoid()
    
    def forward(self,x,hidden) :
        out,hidden = self.lstm(x,hidden)
        out = out[:-1:] # last seq
        out = self.fc(out)
        out = self.sigmoid(out)
        return out,hidden
    
    def init_hidden(self,batch_size) :
        return (torch.zeros(1,batch_size,128).to(device),
                torch.zeros(1,batch_size,128).to(device)
                )


# %%
model = LottoPredictor().to(device)


# %%
criterion = nn.BCELoss()
optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001)
print(model.parameters())
# %% train
num_epochs = 1000
for epoch in range(num_epochs) :
    print(f'train...{epoch}')
    #...todo...


# %%
