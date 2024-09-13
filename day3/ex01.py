#%%
_a = lambda x : x**2

print(_a(8))
# %%

_sum = lambda x,y : x+y
print(_sum(2,3))
# %%
def _inc(n) :
    return lambda x : x+n

__inc3 = _inc(3)

print(__inc3(6))


# %%
__inc2 = _inc(2)
print(__inc2(3))


# %%
a = [1,2,3]
b = [4,5,6]

print(list(map(lambda x,y:x+y,a,b)))
# %%
_list = [5,8,2,6,1,9,3,7,4]

_new_list = list(map(lambda x: 0 if x<=3 else 1,_list))

print(_new_list)

# %%
_list = [5,8,2,6,1,9,3,7,4]
_new_list = list(filter(lambda x: x>3,_list))
print(_new_list)
# %%
