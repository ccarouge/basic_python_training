#%% [markdown]
# # Other built-in types
# 
# Python obviously has a lot of objects built-in. Here we are going to have a quick look at those you are most likely to use at the start. 
# 
# In this notebook, we'll see:
#  - lists
#  - tuples
#  - dictionaries
#  - copy vs. pointers
#  - some interesting methods of these builtin types (including strings) as exercises. 
#%% [markdown]
# ---
# # Lists
#%% [markdown]
# Lists look like arrays but are not arrays! Lists can contain elements of different types and are always 1 dimension.
# 
# A list can probably have any object as an element: other lists, strings, numbers, arrays, functions etc. A list simply allows you to create a collection of objects. It doesn't inform you in any way how these objects are related to each other (or if indeed they are related).

#%%
l = [] # Empty list
l = ['a',1]  # List of 2 elements
print("First list length: ",len(l))
l = [['a','b'],3]  # A list can have another list as an element. But l is still a 2 elements list.
print("I'm still 2 elements long: ", len(l))
l.append(5)
print("Easy to add elements to lists: ", l)

#%% [markdown]
# Lists are indexable. List elements can be changed, i.e lists are mutable objects:

#%%
print(l[0])
l[0]='new'
print(l[0])

#%% [markdown]
# If you have a subscriptable object as a list element, how do you access this element's subscripts? For example, you have the word "new" in the first element of a list and you want to know the last character:

#%%
l[0][-1]


#%%
# Returns an error with non-subscriptable objects
l[1][-1]

#%% [markdown]
# ## Convert to list
# You can convert an iterable object to a list with the builtin function: `list()`. 
# Each element of the initial object will become an element in the list:

#%%
a = "Claire"
b = list(a)
print(b)

#%% [markdown]
# ---
# # Tuples
# 
# Tuples are like lists but are immutable. That means elements of a tuple can't be changed, added, removed. It can be useful for a collection of objects you don't want to inadvertently change in your code. For example, a collection of names of experiments, paths, models etc. Although tuples are rarely used and people tend to simply use lists.

#%%
t = ()  # Empty tuple
t = (1,2,3)
t = 4,5,6  # Parentheses are optional!
t = 1,  # Don't forget the comma to define a 1-element tuple!


#%%
t


#%%
# As said earlier, they are immutable
t=1,2,3
t[0]=3

#%% [markdown]
# ## Convert to tuple
# Same as lists, you can convert interable objects to tuples with the builtin function: `tuple()`.

#%%
a = [1,3,4]
b = tuple(a)
b

#%% [markdown]
# ---
# # Copy or not?
# There is another consequence to all this talk about mutable or immutable. It has to do with how Python manages memory. 
# To reduce the memory footprint of a program, Python will try to make pointers instead of copying the same values at different places in memory.
# That means if 2 variables are the same mutable object both will change if an element of one is changed.
# If one of the object is assigned to something else, then only this object will change.
# Let's see what this means with an example for a list

#%%
# If we change the first element of one list, the other one changes too.
l = [1,2,3]
ll = l
ll[0]=2
print(l, ll)

#%%
# If we reassign l to a different list (even if it's the same as initially), only l changes.
l = [1,2,3]
print(ll,l)

#%% [markdown]
# Since it is impossible to change only 1 element of an immutable object, any change made on those isn't reflected to other objects initially pointing to the same memory.

#%% [markdown]
# ---
# # Dictionaries
# 
# Dictionaries allow you to label values. For example, if you'd like to keep track of a grid description (rectilinear), you might need a grid name, first lon/lat, the resolution, last lon/lat. A dictionary allows you to keep all those values together in one object and allows you to refer to each by name instead of position for example.

#%%
d={
    "name":"my_grid",
    "first_lon":-180.,
    "first_lat":-90.,
    "last_lon":180.,
    "last_lat":90.,
    "res":0.5
}
d


#%%
d["name"]

#%% [markdown]
# The values associated to each key can be very complicated objects. For example, we could have only "first_point" and "last_point" keys, each pointing to a dictionary with lat and lon as keys:

#%%
point0={"lon":-180., "lat":-90.}
point1=point0.copy()
point1["lon"]=180.
point1["lat"]=90.
print(point0, point1)


#%%
d={'name':"my_grid", "first_point":point0, "last_point":point1, "res":0.5}
d["first_point"]

#%% [markdown]
# If you have several grids you want to keep track of. Each key could have a list of values (or tuples). Or you could create a list of dictionaries. So you have 1 dictionary per grid and you keep them all together in a list (or tuple). The second option might be better as it allows you to create a dictionary for a new grid more easily. Copy one of the dictionary and change only the keys you need for the new grid. Then append to the list.

#%% [markdown]
# ---
# These are all the concepts we wanted to introduce.
# As a summary we've seen:
#  - strings, lists, tuples, dictionaries
#  - Builtin functions: 
#     - print()
#     - len()
#     - any()
#     - all()
#     - list()
#     - tuple()
#     - dict()
#
#    For additional builtin functions: https://docs.python.org/3/library/functions.html

#%%
