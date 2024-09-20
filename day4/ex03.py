#%%
import numpy as np
print("numpy version : ", np.__version__)
# %%
_list = [
    [[1,2,3,4]],
    [[5,6,7,8]],
    [[9,10,11,12]]
]

a1 = np.array(_list)
print(a1)
print(a1.shape)
# %%
print(a1[0])
# %%
print(a1[0:])
# %%
print(a1[0,0,1])

# %%
print(a1[1,0,1])
print(a1[2,0,2])
# %%
print(a1[0,0,2:4])
# %%
