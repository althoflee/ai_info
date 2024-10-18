#%%
import torch
import torch.nn as nn
import torch.optim as optim

import math
import matplotlib

import matplotlib.pyplot as plt

print(torch.__version__)
#%%

x= torch.linspace(0,2*math.pi,1000).unsqueeze(1)
y= torch.sin(x)
#%%
# print(x)
# %%
class SimpleSineModel(nn.Module) :
    def __init__(self) :
        super(SimpleSineModel,self).__init__()
        
        self.fc1 = nn.Linear(1,16)
        self.fc2 = nn.Linear(16,32)
        self.fc3 = nn.Linear(32,16)
        self.fc4 = nn.Linear(16,1)
        self.relu = nn.ReLU()
        
    def forward(self,x) :
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.relu(self.fc3(x))
        x = self.fc4(x)
        return x
    
simple_model = SimpleSineModel()
#%%
learning_rate = 0.01
epochs = 50000
optimizer = optim.Adam(simple_model.parameters(),lr=learning_rate)
loss_fn = nn.MSELoss()

#%%
loss_values = []
for epoch in range(epochs) : 
    optimizer.zero_grad()
    y_pred = simple_model(x)
    loss = loss_fn(y_pred,y)
    loss.backward()
    optimizer.step()
    
    loss_values.append(loss.item())
    if epoch % 500 == 0 :
        print(loss.item())
    
    
# %%

plt.figure(figsize=(10,5))
plt.plot(range(epochs),loss_values,label='loss',color='green')
plt.legend()
plt.show()
# %%
x_test= torch.linspace(0,2*math.pi,1000).unsqueeze(1)
y_test=simple_model(x_test)

plt.figure(figsize=(10,5))
plt.plot(x_test,y_test.detach().numpy(),color='blue')

plt.legend()
plt.show()
# %%
