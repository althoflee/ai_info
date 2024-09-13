#%% unpack
_list = [1,2,3,4,5,6]

a = _list[0]
b = _list[1]
print(a,b)

# %%
a,b,c,d,_,_ = _list
print(a,b)
# %%
a,b,c,d,*_ = _list
print(c,d)
# %%
*a, = _list
print(a)
# %%
_,_,a,b,_,_ = _list
print(a,b)
# %%
_,_,a,b,*_ = _list
print(a,b)
# %%
_,_,*a,_,_ = _list
print(a)
# %%
_list = [1,2,3]
#%%
print(_list)

# %%
_list.append(77)

# %%
_list.insert(0,88)
# %%
_list.insert(-1,88)
# %%
_list.insert(1,88)
# %%
print(_list.pop())
# %%
print(_list.pop(0))
# %%
