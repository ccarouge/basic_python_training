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
# To keep the string together as 1 element of the list:
c = [a]
print(c)
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
print(b)
# Here again if you want to keep the list as an element of the tuple:
c = (a,)
print(c)
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
# The easiest way to make a copy of a mutable object is with the `list()` and `dict()` functions (see below for `dict()`).
# These will only do a shallow copy of the object. It is usually enough.
# There are ways to make deep copies of mutable objects. That is rarely needed, we'll see it at the end, depending on time.
#
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
point1=dict(point0)
point1["lon"]=180.
point1["lat"]=90.
print(point0, point1)
#%%
d={'name':"my_grid", "first_point":point0, "last_point":point1, "res":0.5}
d["first_point"]
#%% [markdown]
# ## Get the keys and values
# %%
# Get the keys in a dictionary:
for k in d.keys():
    print(k)
print("End keys \n")

# Get the values:
for v in d.values():
    print(v)
print("End values \n")

# Get the pairs of keys and values:
for k,v in d.items():
    print(k,v)
print("End pairs \n")

# As you can see here, loops in Python can have several loop variables!
#%% [markdown]
# ## Add a (key,value) pair
#%%
d['projection'] = "cartesian"
d
#%% [markdown]
# If you have several grids you want to keep track of, each key could have a list of values (or tuples). Or you could create a list of dictionaries. So you have 1 dictionary per grid and you keep them all together in a list (or tuple). The second option might be better as it allows you to create a dictionary for a new grid more easily by simply appending its definition dictionary to the list.
#%% [markdown]
# ---
# # Exercises
# Below are a few exercises or examples for you to go through.
# 
# Don't forget to use either the inline help (?var or <tab>) or Google and Stack Overflow.
# %% [markdown]
#  ## String formatting with dictionaries
# We saw earlier that f-strings are the most readable way to format a string.
# 
# With dictionaries, `str.format()` can be quite powerful and useful:
# %%
# Let's define a dictionary:
point0=[-180., -90.]
point1=[180.,90.]
d={'name':"my_grid", "first_point":point0, "last_point":point1, "res":0.5}
print(d)
# Let's print all this information nicely with f-string and then `str.format()`
print(f"My string {d['name']} has {d['res']} degrees resolution, starts at {d['first_point']}, ends at {d['last_point']}")
print("My string {name} has {res} degrees resolution, starts at {first_point}, ends at {last_point}".format(**d))
#%% [markdown]
# The ** operator allows us to take a dictionary of key-value pairs and unpack it into keyword arguments in a function call.
# There is also a `*` operator.
# See this page for details: https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/
# This page is using a few things we haven't seen but it's very thorough.
#%% [markdown]
# ---
# ## Split and join strings
# If reading tabulated data or a filename with fields separated by "_", it's common one might want to split the different fields into separate strings or values.
# Inversely, you might want to create files that have fields separated by "_". You can use `+` to add the different fields, but it gets long pretty quickly. Python provides a better way.
#%%
# Split the following string along the "_" separator. Hint: check the string's methods. What is the type of the result?
a="tas_day_MRI-ESM1_historical_r1i1p1_18510101-18601231.nc"
#%%
# Join together the elements of the following list to form a filename with the same format as above.
# Again check the string's methods. Be careful how you specify the separator and the strings to join!
l = ["ta", "day", "ACCESS", "historical","r1i1p1", "18510101", "19001231","nc"]
#%% [markdown]
# ---
# ## Zip function
# It allows you to zip together 2 iterables. So that the first elements of the 2 original iterables become together the 1st element of the result, etc.
# 
# Obviously, it's much easier to see examples.
#
#%%
a="Claire"
b="Carouge"
c=list(zip(a,b))
c
#%%
# Given the 2 lists below, create a dictionary where the keys come from the list "keys" and values from "values"
keys=['name', 'age', 'place']
values=['John', 32, 'Paris']
#%% [markdown]
# ---
# These are all the concepts we wanted to introduce.
# As a summary we've seen:
#  - strings, lists, tuples, dictionaries
#  - how to format strings with `str.format()` and f-strings
#  - Builtin functions: 
#     - print()
#     - len()
#     - any()
#     - all()
#     - list()
#     - tuple()
#     - dict()
#  - For loops
#  - If constructs
#  - A few useful methods and other builtin functions in the exercises.
#    For additional builtin functions: https://docs.python.org/3/library/functions.html
#%%