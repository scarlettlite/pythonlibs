"""
Notes on python's Set
Underlying Data Structure: Hashtable
Set is a unordered mutable type. 
It does not support operations like slicing and indexing
Methods like union, intersection, difference, symmetric_difference,
isdisjoint, issuperset, issubset, update, intersection_update,
difference_update and symmetric_difference_update 
can accept non set iterables as 
arguments unlike their operator versions
set is an iterable
"""

"""
Set API's that dont change the underlying object
"""

"""
create an empty set
"""
ss = set()

"""
create a non-empty sey
"""
ss = set(range(7))
ss = {'567', '890', '890'}  # an alternative to create a non empty set
ss = {} # this creates an empty dictionary not a set


s = set(range(25))

"""
get the length of a set
"""
print(len(s)) #25


"""
in/ not in
"""
print(1 in s) # True
print(34 not in s) # True


"""
Beginning of list of functions that dont change the underlying set
These functions are also applicable to frozenset
"""

"""
Return True if the set has no elements 
in common with other
"""
print(s.isdisjoint(set(range(56,89)))) # True

"""
Test whether the set is the subset of other
"""
print(s.issubset(set(range(25)))) # True
print(s <= set(range(35))) # True


"""
Test whether set is the proper subset of other
"""
print(s < set(range(30))) # True
print(s < set(range(25))) # False

"""
Test whether set is the superset of other
"""
print(s >= set(range(25))) # True
print(s.issuperset(set(range(15)))) # True

"""
Test whether the set the proper superset of other
"""
print(s > set(range(23)))  # True
print(s > set(range(25))) # False

"""
Return a new set with elements from the set and all
other sets. Note here union doesn't change the underlying
objects
"""
x, y = set(range(23)), set(range(20,30))
newset = s.union(x,y) # does not make any changes to set s
newset = s | x | y
#newset = {1,2...,29}


"""
Return a new set with elements common to this set and all others
"""
x, y = set(range(23)), set(range(20,30))
newset = s.intersection(x,y)
newset = s & x & y #newset = {1,2,...24}


"""
Return elements that are in set and not in others
"""
x, y = set(range(23)), set(range(20,30))
newset = s.difference(x,y)
newset = s - x - y # newset = set()

"""
Return elements which are in exactly one of the sets
symmetric_difference can take only one set as argument
"""
x,y,z = set(range(7)), set(range(6,10)), set([5,8,12])
newset = x.symmetric_difference(y) # {0, 1, 2, 3, 4, 5, 7, 8, 9}
newset = x ^ y ^ z # {0, 1, 2, 3, 4, 7, 9, 12}

"""
Return a new shallow copy of set
"""
newset = s.copy()
"""
End of methods that do not change the underlying set object
"""


"""
Beginning of set of Methods that change the underlying set 
"""
"""
Update the set adding elements from all others
"""
s = set(range(7))
s.update(range(10,15), range(25,30))
s |= set(range(10,15)) | set(range(25,30))
# s = {0, 1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 25, 26, 27, 28, 29}

"""
Update the set only keeping elements that appear in all others
"""
s = set(range(7))
s.intersection_update(range(5,10), range(1,10))
s &= set(range(5,10)) & set(range(1,10))
# s = {5, 6}

"""
Update the set with elements that do not occur in other sets
"""
s = set(range(7))
s.difference_update(range(5,10)) #s = {0, 1, 2, 3, 4}
s -= set(range(5,10)) # | others


"""
Update the set keeping only those elements that occur exactly in one of the
sets
"""
s = set(range(7))
s.symmetric_difference_update(range(5,10)) #s = {0, 1, 2, 3, 4, 7, 8, 9}
s ^= set(range(5,10)) # | others

"""
Remove an element 'e' from set if e is present
"""
s = set(range(7))
s.discard(8) # does not throw a key error
#s.remove(8) # throws a key error if 8 is not in the set

"""
Remove an arbitrary element from the set
"""
s.pop()

"""
clear all elements from a set
"""
s.clear()


"""
print all elements in a set
"""
s = set(range(9))
for x in s:
    print(x)