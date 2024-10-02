#%%
import numpy as np

#%%
gate_data = np.loadtxt('./gate.csv',delimiter=',',dtype=np.int8,skiprows=1)
print(gate_data)
# %%
print(gate_data[:,0:2])
# %%
print("and : ",gate_data[:,2])
# %%
print("or : ",gate_data[:,3])
print("xor : ",gate_data[:,4])
# %%
