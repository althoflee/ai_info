#%%
import numpy as np

#%%
x1 = np.random.randint(0,100,10)
print(x1)

# %%
print("sum :" , x1.sum())
print("avg :", x1.mean())
print("standard : " , x1.std())
print("var : " , x1.var())
# %%

x2 = np.array([
    np.random.randint(0,100,10),
    np.random.randint(0,100,10)    
])

print(x2)

# %%
print(x2.sum())
# %%
