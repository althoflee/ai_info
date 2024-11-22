#%%
import torch
from torch.utils.data import Dataset,DataLoader

import torch.nn as nn
import torch.optim as optim

print('module load complete')
print(f'torch version : {torch.__version__}')

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f'device : {device}')

#%%
class XORModel(nn.Module) :
    def __init__(self) :
        super(XORModel,self).__init__()
        self.layer1 = nn.Linear(2,4)
        self.layer2 = nn.Linear(4,1)        
        self.active = nn.Sigmoid()
    def forward(self,x) :
        x = self.active(self.layer1(x))
        x = self.active(self.layer2(x))
        
        return x

model = XORModel()
#%% load data
dataset = torch.load('xor_dataset.pth')

#%%
batch_size = 4
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(),lr=0.1)
dataloader = DataLoader(dataset,batch_size)

#%% train
num_epoch = 100000
for epoch in range(num_epoch) :
    for X,Y in dataloader:
        
        #순전파
        _Y = model(X)
        loss = criterion(_Y,Y)
        
        #역전파
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
    if (epoch+1) % 10000 == 0 :
        print(f' loss {loss.item()}')
        
        




# %%
