#%%
import numpy as np
print("numpy version : ", np.__version__)

#%%
a1 = np.array([3,4])
a2 = np.array([5,6])

print(a1+a2)
print(a1/a2)
print(a1*a2)
# %%
a1 = np.zeros(10,dtype=np.uint8)
print(a1)

print(a1.shape)
print(a1.dtype)


# %%
a2 = np.arange(0,10,1,dtype=np.float32)
print(a2.shape)
print(a2.dtype)
print(a2[3:7])
# %%
print(a2)
print(a2.reshape(5,2))
print(a2.reshape(2,5))

# %%
print(np.random.rand(10))
# %%
a3 = np.random.rand(10)
print(a3)
# %%
_a3 = a3*100
print(_a3)
# %%
__a3 = _a3.astype(np.int32)
print(__a3)
# %%
