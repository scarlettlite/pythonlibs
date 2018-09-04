"""
dict constructor
create dicts from kwargs, mappings, and iterable 
for iterables in which each object is an iterable of exactly two objects
"""
a = dict(one=1, two=2)
b = dict(zip(['one', 'two'],[1,2]))
c = dict((('one',1),('two',2)))
print(a==b==c)

"""
if kwargs is provided along with the positional arguments
then value in kwargs will overwrite the values in positional arguments
"""
a = dict(zip(['one', 'two'], [1,2]), one=3)
print(a)

"""
Beginning of operations supported by dictionary
Only operations that I find hard to remember are mentioned here
"""

# return an iterator over the keys object
iter(a.keys())

#clear all key-value pairs
a.clear()

#return a shallow copy of the dictionary
a.copy()

#classmethod fromkeys, return a dictionary with key values from iterable
#each key has value as the second argument
print(dict.fromkeys([1,2,3], 'alpha'))

#return a dynamic dictionary view of key value pairs.
#dynamic view means, when the dictionary is updated this object will
#reflect those changes. This is not an inter object
a.items()
a.keys()
a.values()

#pop a key named 'one' and return the value . if key is not found then 
#key error is raised
a.pop('one')

#remove a (key,value) pair from dictionary. the items in LIFO order from version 3.7
#raises a key error if the key if empty
a.popitem()

#if key is in dictionary return value, else set the default value given and return it
a.setdefault('one', 1)

#extend dictionary with key, values pairs. overwrite any existing keys
a.update(dict())
a.update(one=1,four=4)
a.update([]) #iterable where each element is an iterable of length 2

#dictionaries only implement equal to other comparisons will throw a ValueError
#two dictionaries are equal if all their key value pairs are equal
a == b

#order of keys is LIFO as in 3.7. When keys are updated order is not changed.
#if a key is deleted and then added again, then the order changes
"""
End of operations supported by dictionary
"""


"""
Dictionary view Objects
"""
"""
Dictionary view objects support iteration and support membership tests
Do not try to delete or add items in a dictionary while iterating through it
This may cause an undefined behavior or may throw a run time error
Key view are set like because all items are hashable
value and (key, value) view can also be set like if values are hashable.
In this case order operations like <, <= etc will also be supported
"""




"""
End of operations supported by dictionaries
"""