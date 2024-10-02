#%%
import torch
import torch.nn as nn

#%%
torch.set_printoptions(precision=4)
#%% xor
X = torch.tensor([[0,0],[1,0],[0,1],[1,1]],dtype=torch.float32)
Y = torch.tensor([[0],[1],[1],[0]],dtype=torch.float32)

print(X,Y)

# %% model
class NeuralNet(nn.Module) :
    def __init__(self,input_size,hidden_size,num_classes) : 
        super(NeuralNet,self).__init__()
        self.input_size = input_size
        self.l1 = nn.Linear(input_size,hidden_size)
        self.relu = nn.ReLU()
        self.l2 = nn.Linear(hidden_size,num_classes)
    def forward(self,x) :
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        return out
    
    
model = NeuralNet(2,10,1)
# %% 학습준비
learning_rate = 0.01
n_iters = 1000

loss = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(),lr=learning_rate)

#%% 학습
for epoch in range(n_iters) :
    y_predicted = model(X)
    
    #loss
    l = loss(Y,y_predicted)
    l.backward()
    
    optimizer.step()
    
    optimizer.zero_grad()
    
    if (epoch %100 == 0) :
        print(l.item())


# %%

pred = model(torch.tensor([1,0],dtype=torch.float32))
print(pred)
             

# %%
