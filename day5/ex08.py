#%% shape
import numpy as np

#%%
x1 = np.random.randint(0,100,16)
print(x1)
print(x1.shape)
# %%
_x1 = np.expand_dims(x1,axis=0)
print(_x1)
print(_x1.shape)

#%%
_x1 = np.expand_dims(x1,axis=1)
print(_x1)
print(_x1.shape)


# %%
x2 = np.reshape(x1,(4,4))
print(x2)
print(x2.shape)

# %%
x3 = np.reshape(x1,(-1,8))
print(x3)

