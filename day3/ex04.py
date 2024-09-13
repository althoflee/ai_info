#pip install numpy
#%%
import sys
import numpy as np
print(sys.version)
print(np.__version__)
#%%
a = np.empty(0)
print(a)
# %%
a = np.append(a,1)
print(a)
#%%
_list1 = [1,2,3,4]
arry1 = np.array(_list1)
print(arry1)

# %%
print(arry1.shape)
# %%
print(arry1[0:2])    
# %%
print(type(arry1))
print(arry1.dtype)

# %%
_arry1 = arry1.astype(np.float16)
print(_arry1)

# %%
arry2 = np.array([1,2,3])
arry3 = np.array([4,5,6])

print(arry2+arry3)
# %%
