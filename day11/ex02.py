#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn as nn

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

#%% gpu check
# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

device = torch.device('cpu')

print(device)

#%%
print(f"cuda version {torch.version.cuda}")
print(f"device count {torch.cuda.device_count()}")
print(f"device name : {torch.cuda.get_device_name(0)}")
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

X_train = torch.tensor(X_train,dtype=torch.float32).to(device)
y_train = torch.tensor(y_train,dtype=torch.float32).to(device)
X_test = torch.tensor(X_test,dtype=torch.float32).to(device)
y_test = torch.tensor(y_test,dtype=torch.float32).to(device)

#%%

print(X_train.shape)
print(X_test.shape)

print(y_train.shape)
print(y_test.shape)

# %%
class LottoLSTM(nn.Module):
    def __init__(self, input_size,hidden_size,output_size,num_layers) :
        super(LottoLSTM,self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_size,hidden_size,num_layers,batch_first=True)
        self.fc = nn.Linear(hidden_size,output_size)
    def forward(self,x) :
        h0 = torch.zeros(self.num_layers,x.size(0),self.hidden_size).to(device)
        c0 = torch.zeros(self.num_layers,x.size(0),self.hidden_size).to(device)
        out,_= self.lstm(x,(h0,c0))
        out = self.fc(out[:,-1,:])
        return out

model = LottoLSTM(7,64,7,2)
#%%
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(),0.001)

#%% train
num_epochs = 5000
for epoch in range(num_epochs) :
    model.train()
    outputs = model(X_train)
    loss = criterion(outputs,y_train)
    
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    if epoch % 10 == 0 :
        print(f'Epoch [{epoch}/{num_epochs}] ,loss :{loss.item():.4f}')

# %%
model.eval()
with torch.no_grad() :
    test_outputs = model(X_test)
    test_loss = criterion( test_outputs, y_test)
    print(f'Test loss : {test_loss.item():.4f}')


# %%
X_Tensor = torch.tensor(X,dtype=torch.float32)
last_sequence = X_Tensor[-1].unsqueeze(0)
#%%
print(last_sequence)
# %%
with torch.no_grad():
    next_pred = model(last_sequence)

# %%
print(next_pred)
# %%
pre_nums = scaler.inverse_transform(
    next_pred.detach().numpy())
#%%
print(np.round(pre_nums[0]).astype(int)+1)
# %%
def pridictData(seq_index) :
    if seq_index < len(X) :
        # GT ,실제 데이터
        input_seq = X[seq_index]
        actual_output = y[seq_index]
        
        input_seq = torch.tensor(input_seq,dtype=torch.float32).unsqueeze(0).to(device)
        actual_output = torch.tensor(actual_output,dtype=torch.float32).unsqueeze(0).to(device)
        
        #모델 예측
        model.eval()
        with torch.no_grad() :
            predict_output = model(input_seq)
        
        np_predict = predict_output.cpu().detach().numpy()
        np_actual = actual_output.cpu().detach().numpy()
        
        predict_numbers = np.round(scaler.inverse_transform(np_predict)).astype(int)
        actual_numbers = np.round(scaler.inverse_transform(np_actual)).astype(int)
        
        return predict_numbers[0],actual_numbers[0]
    else :
        return None
#%%
_pre,_gt = pridictData(600)
print(_pre)
print(_gt)        
        
        



# %%
