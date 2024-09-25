#%%
import numpy as np

#%%
x1 = np.random.randint(0,100,10)
x2 = np.random.randint(0,100,10)

print(x1,x2)
# %%

x3 = np.array([_v for _v in zip(x1,x2)])
print(x3)
# %%
x4 = np.array([_v for _v in zip(x1,x2) if _v[0] < 50 ])
print(x4)
# %%
