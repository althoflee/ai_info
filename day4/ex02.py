#%%
import numpy as np
print("numpy version : ", np.__version__)
#%%
a1 = np.arange(0,10,1)
print(a1)
print(a1[0:5])
# %%
_list = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

a2 = np.array(_list)

print(a2)
print(a2.shape)
# %%
print(a2[2,0])
print(a2[2,:])
print(a2[:,1])
print(a2[:,0:2])
print(a2[:,2:4])
# %%
print(a2)
# %%
