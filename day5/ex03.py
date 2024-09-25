#%% 2d array sort
import numpy as np
#%%
x1 = np.array([
    [1,9],
    [0,8],
    [6,3],
    [3,4],
    [4,1]]
)

print(x1)
# %%
print(x1[:,0])
print(x1[:,1])
# %%
print(x1[:,0].argsort())
_sort_indice = x1[:,0].argsort()
print(x1[:,0][_sort_indice])

#%%
print(x1[:,1].argsort())
_sort_indice2 = x1[:,1].argsort()
print(x1[:,1][_sort_indice2])

# %%
