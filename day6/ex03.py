#%% 
import numpy as np
import matplotlib.pyplot as plt
#%%
x = np.linspace(0,10,50)
y = 2*x+ (1 + np.random.randn(50))

# print(x,y)

# %%
A = np.vstack([x,np.ones(len(x))]).T
# print(A)
a,c = np.linalg.lstsq(A,y,rcond=None)[0]
print(f"기울기 {a} , 절편 {c}")

# %%
plt.scatter(x,y,label='data point')
plt.plot(x,a*x+c,'r',label='fiting line')
plt.legend()
plt.show()


# %%
