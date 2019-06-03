#%% [markdown]
# # Let's start with strings
# 
# We assume you know how to program. You don't need to learn what a loop or a variable is!
# 
# We are starting with strings as this is a type common to most languages so you likely know what it is. But they also allow us to introduce lots of Python concepts!
# 
# Using strings, we'll have a look at the following:
#  - what object-oriented language means
#  - the print() function and how to format a string
#  - indexing
#  - loops
#  - if constructs

#%%
# First variable
a = "Claire"
#%%
a  # Easy to get the value of a variable in a notebook
#%%
# Can be done in one cell:
a = "Claire"
a
#%%
# Python is case sensitive
A
#%% [markdown]
# ## Object-oriented language
# 
# Everything is an object in Python. That means a variable contains more than a value. It may also contain:
#  - **functions, called methods**. These are specific to each object type. A string and an array won't have the same methods.
#  - **attributes**. These are additional information about the object. Think of it a bit like meta-data. Attributes differ from methods because they simply contain a value and not a function.
#%%
# Find out the type of an object
?a
#%%
type(a)
#%%
# Find all attributes/methods of an object
dir(a)
#%% [markdown]
# It doesn't tell you if those are methods or simple attributes. There is no information on what the method does. Inline help can help here.
#%% [markdown]
# ## Print function
#%% [markdown]
# Obviously, there is a `print()` function builtin. It can print out the values in all sorts of objects, not just strings.
#%%
print(a)
#%%
# Print several variables together:
print("My var is:",a)
#%%
b = "it's me"
print(a,",",b)
#%% [markdown]
# ### Formatting
# It is possible to format a string in Python and there are several ways to do that.
# 
# Let's start by the old way you shouldn't use. We only see it because you might encounter it:
#%%
a=100.
print("It's %s dollars"%a)
#%% [markdown]
# For a newer method of formating, use: `str.format()`
#%%
print("It's {} dollars".format(a))
#%% [markdown]
# When putting several variables into the same string, it allows you to refer to the `str.format()` arguments by position or name:
#%%
a=100.
b=50
print("It's {1}% off, it costs {0} dollars".format(a,b))
print("It's {perc}% off, it costs {cost} dollars".format(perc=b, cost=a))
#%%
print("It's {:3.0f} dollars".format(a))
#%% [markdown]
# As you can see above, it is possible to describe the format of the variable in the string.
# Here we said we wanted a fixed-point notation, with an overall width of 3 charaters and 0 characters after the decimal point (called the precision). 
#
#  There are lots of possibilities to format strings. Python refer to it as "Format Specification Mini-Language".
# The complete documentation is here: https://docs.python.org/3/library/string.html#formatspec
#
#  A few examples below:
#%%
# Pad a number on the left with zeros. Remember the type of your variable!
b="{:0>6}".format(a)
c="{:0>6.0f}".format(a)
print(b)
print(c)
#%%
# Exponent notation:
print("{:e}".format(a))
print("{:.3e}".format(a))
#%% [markdown]
# ## Indexing
# 
# Strings are indexable in Python. Indexes start at 0 in Python. It's possible to have negative indexes, thus `-1` refers to the last element.
#%%
a = 'Claire'
a[1]
#%%
a[-1]
#%%
a[-3]
#%% [markdown]
# ### len() function
#%% [markdown]
# This is a builtin function in Python. It returns the length of a whole bunch of objects. Be careful when using it with more complex objects as it might not return what you'd like as we'll see later
#%%
len(a)
#%% [markdown]
# ### Slicing
#%%
print(a[0:1]) # Last index isn't included. Same as a[0]
print(a[0:3])
print(a[:3]) # Start and end indexes can be omitted. This means everything from start to index 3-1
print(a[3:]) # Means everything from index 3 to the end.
print(a[::2]) # You can use a stride. It means from start to end, print every other character.
print(a[0:-1]) # That's not the whole string!
print(a[:-1]) # This neither
print(a[0:len(a)]) # The whole string
print(a[0:len(a)-3]) # You can obviously have expressions to define the indexes
#%% [markdown]
# The slice `0:3` means, “Start at index 0 and go up to, but not including, index 3.” The up-to-but-not-including takes a bit of getting used to, but the rule is that the difference between the upper and lower bounds is the number of values in the slice.
# 
# But it's nice as it avoids having a `-1` all the time. For example, to get the 3 first character, you use this slice `:3`. If the last index was including, you would need: `:3-1`. If you want 2 characters from the 2nd character, you do `2:2+2` and not `2:2+2-1`. Etc.
#%% [markdown]
# # Loops
#%% [markdown]
# You can loop on any iterable! No just a range of numbers.
#%%
for char in a:
    print(char)
#%% [markdown]
# Note the syntax! `for`, `in`, `:`, indentation to define what is in the loop.
#%%
for char in a:
    print("Indentation = in the loop")
    print("Still in")
print("This is outside the loop because less indented")
#%%
# Different indentations = error
for char in a:
    print("Hey")
        print("OK?")
#%% [markdown]
# ### Loop over a range:
#%%
for i in range(3,17,2):   # End index is excluded here again! There is some consistency.
    print(i)
#%%
for i in range(5):
    print(i)
#%%
# Nested loop
for i in range(2):
    for char in a[:3]:
        print(char)
    print("Index:",i)  # In outer loop but not inner loop
#%%
# Break / continue statements
for i in range(10):
    if i == len(a):
        break
i
#%% [markdown]
# There is also a `while` construct, which you can discover on your own. It has a similar syntax as the `for` loop construct.
#%% [markdown]
# ## If constructs
#%%
if "l" in a:
    print("Yeah")
#%%
if "Claire" == a:
    print("Yeah")
#%%
# Negation
if "Claire" != a:
    print("yeah")
if not "z" in a:
    print("oh!")
#%%
# and / or
if not "z" in a and "l" in a:
    print("yeah")
#%% [markdown]
# A lot more details on comparison expressions: https://docs.python.org/3/reference/expressions.html#comparisons
# 
# And operator precedence: https://docs.python.org/3/reference/expressions.html#operator-precedence
#%% [markdown]
# ### any() and all() functions
# 
# Python has `any()` and `all()` functions as built-in. 
# 
# `any(x)` returns true if at least 1 value in x is True, 
#
#  `all(x)` returns true if all values in x are True or x is null.
# 
# In Python, 0, False and None are False. Everything else is True
#%%
all(a)
#%%
b=""
print(all(b), any(b))