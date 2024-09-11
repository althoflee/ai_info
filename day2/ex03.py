# github repo url : https://github.com/althoflee/ai_info
#%%
_tuple = (1,2,3,4,5,6)
print(_tuple)

#%% 
print(_tuple[3])
_tuple[3] = 0

# %%
_tuple = (v for v in range(10))
print(_tuple)
# %%
_list = [1,2,3]
print(_list)
print(_list[2])
#%%
_list[2] = 7
print(_list[2])


# %%
print(_list)

# %%
_list = [v for v in range(10)]
print(_list)
# %%
__list = [_list]
print(__list)
# %%
print(__list[0])
print(__list[0][1])
# %%
_list1 = [1,3,5,7,9]
_list2 = [2,4,6,8,10]

print( _list1 + _list2)

# %%
poly = [(x+y) for x,y in zip(_list1,_list2)]
print(poly)

# %%
