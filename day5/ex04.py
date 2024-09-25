#%% 2d array sort
import numpy as np

#%%
x1 = np.array( [    
        [[102,131]],
        [[101,237]],
        [[148,11]],
        [[24,189]],
        [[247,19]]
])
print(x1)

# %%
print(x1[:,0,0])
print(x1[:,0,1])
# %%
sort_indice = x1[:,0,0].argsort()
print(sort_indice)
print(x1[:,0,0][sort_indice])
# %%
print(x1[0,0,:])
# %%
