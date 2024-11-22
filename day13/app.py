#%%
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset,DataLoader

from datautil import LottoDataset,getLottoDataset
#%%

batch_size = 64
train_data,test_data,val_data = getLottoDataset()

train_loader = DataLoader(train_data,batch_size,shuffle=False)
test_loader = DataLoader(test_data,batch_size,shuffle=False)
val_loader = DataLoader(val_data,batch_size,shuffle=False)

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
#%%
def calculate_correct_numbers(output,y_batch,k) :
    _,topk_indice = torch.topk(output,k,dim=1)
    preds = torch.zeros_like(output)
    preds.scatter_(1,topk_indice,1)
    
    num_correct_per_sample = (preds * y_batch).sum(dim=1)
    return num_correct_per_sample.cpu().numpy(),preds



num_epochs = 1000
for epoch in range(num_epochs) :
    print(f'train...{epoch}')
    model.train()
    train_losses = []
    train_correct_numbers = []
    
    for x_batch,y_batch in train_loader:
        x_batch = x_batch.to(device)
        y-batch = y_batch.to(device)
        
        batch_size = x_batch.size(0)
        hidden = model.init_hidden(batch_size)
        
        optimizer.zero_grade()
        output,hidden = model(x_batch,hidden)
        loss = criterion(output,y_batch)
        loss.backward()
        optimizer.step()
        
        hidden = (hidden[0].detach(),hidden[0].detach())
        train_losses.append(loss.item())
        
        num_correct_per_sample , _ = calculate_correct_numbers(output,y_batch,k)
        train_correct_numbers.extend(num_correct_per_sample)
        
    avg_correct_numbers = np.mean(train_correct_numbers)
    print(f"Epoch {epoch+1}/{num_epochs} , Loss : {np.mean(train_losses)}, correct Numbers:{avg_correct_numbers}")
        

# %%
