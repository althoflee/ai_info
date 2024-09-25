#%%
import numpy as np

#%%
x1 = np.random.randint(0,100,10)

print(x1)

# %%
#print([value for value in x1])

_x2 = np.array([value for value in x1])
print(_x2)
# %%

_x3 = np.array([value for value in x1 if value%2])
print(_x3)

# %%
