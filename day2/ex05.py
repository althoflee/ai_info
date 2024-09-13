#%%
_list = [4,8,6,2,1]

print(_list)


# %%
new_list = [i+1 for i in _list]
print(new_list)
# %%
new_list.sort()
print(new_list)
# %%
tensor = [[1,2,3],[4,5,6],[7,8,9]]
print(tensor)
# %%
_tensor = [_t for t in tensor for _t in t]
print(_tensor)

# %%
