#%%
import torch
from torch.utils.data import Dataset,DataLoader

from my_dataset import MyXorDataset

print('module load complete')
print(f'torch version : {torch.__version__}')

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f'device : {device}')

#%%
X = torch.tensor([[0,0],[0,1],[1,0],[1,1]],dtype=torch.float32)
Y = torch.tensor([[0],[1],[1],[0]],dtype=torch.float32)

    
#%%
dataset = MyXorDataset(X,Y)


#%%
dataloader = DataLoader(dataset,batch_size=1,shuffle=False)

for idx,(X,Y) in enumerate(dataloader) :
    print(f"batch idx : {idx}")
    print(f"x : {X}")
    print(f"y : {Y}")



# %%
dataloader = DataLoader(dataset,batch_size=2,shuffle=False)


for idx,(X,Y) in enumerate(dataloader) :
    print(f"batch idx : {idx}")
    print(f"x : {X}")
    print(f"y : {Y}")
# %%

dataloader = DataLoader(dataset,batch_size=3,shuffle=False)

for idx,(X,Y) in enumerate(dataloader) :
    print(f"batch idx : {idx}")
    print(f"x : {X}")
    print(f"y : {Y}")

# %%

dataloader = DataLoader(dataset,batch_size=4,shuffle=False)

for idx,(X,Y) in enumerate(dataloader) :
    print(f"batch idx : {idx}")
    print(f"x : {X}")
    print(f"y : {Y}")
# %% save dataset
torch.save(dataset,"xor_dataset.pth")
