#%% sort
import numpy as np

#%%
x1 = np.random.randint(0,100,10) # 0 ~ 99
print(x1)
# %%
print(np.sort(x1)) # 원본 변화
print(x1)
# %%
print(np.argsort(x1))
print(x1)
sort_indice = np.argsort(x1)
# %%
print("min ",x1[sort_indice[0]])
print("min ",x1[x1.argmin()])
print("max ",x1[x1.argmax()])

# %%
x2 = np.array([0,0,1,0,0,1,0,0,0,0])
print(x1[x2])

# %%
print(x1[sort_indice])

# %%
