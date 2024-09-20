#%%
import numpy as np
print("numpy version : ", np.__version__)
# %%
a1 = np.array([1,2,3,4,5,6])
a2 = np.array([7,8,9,10,11,12,13,14])

print(a1[2:5])
print(a2[3:6])
# %%
a1[2:5] = a2[3:6]
print(a1)
# %%
z1 = np.zeros((3,))
print(z1)

# %%
z2= np.zeros((3,) + (2,2))
print(z2)
# %%
print(z2.shape)
# %%
