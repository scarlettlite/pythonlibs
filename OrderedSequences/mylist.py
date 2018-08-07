"""
List is an ordered mutable iterable sequence
It works like a stack. Inserting or removing at the end are O(1)
operations
Since list is mutable it has no implementation for hash()
"""

el = []
l1 = list(range(3))
l2 = list(range(4,7))
r1 = range(5)
print(1 in l1) # True
print(3 not in l1) # True

"""
Additive and Multiplication Concatenations work on lists
"""
print(l1 + l2) # [0, 1, 2, 4, 5, 6]

"""
Mutiplicative concatenation operator takes the objects inside the 
list and multiplies with them 
"""
print(3 *[1]) #[1,1,1]
print([1] * 3) # [1,1,1]
print([] * 3) # []

"""
[[],[],[]] each list is the reference to the same list . This could lead 
to unpredictable results so use list comprehensions whenever you need 
n-dimensional arrays
"""
print([[]] * 3)   # [[],[],[]]
"" 


"""
slicing by stepping
l[i:j:k]
the default value of i,j depends on sign of k 
if k is negative : i = len(l) - 1, j = -1
if k is positive : i = 0, j = len(l)
"""
l = list(range(25))
print(l[20:4]) # empty
print(l[4:10]) # [4, 5, 6, 7, 8, 9]
print(l[-1::-3]) # [24, 21, 18, 15, 12, 9, 6, 3, 0]
print(l[::-5]) # [24, 19, 14, 9, 4]
print(l[24:5:-2]) # [24, 22, 20, 18, 16, 14, 12, 10, 8, 6]

"""
if we referenced an object at index >= len(l), This will throw a value
error
"""
l = []
try:
    x = l[0]
except:
    print("referenced an object at index >= len(l)")


"""
Functions that can be called with lists as arguments
"""
l = list(range(10))
len(l) # 10
max(l) # 9
min(l) # 0


"""
Beginning of Functions that mutate a list
"""

"""
replace slice of a list
"""
l[4:] = list(range(4)) # l = [0, 1, 2, 3, 0, 1, 2, 3]
l[4:5] = list(range(4)) # l = [0, 1, 2, 3, 0, 1, 2, 3, 5, 6, 7, 8, 9]

"""
both resulting lists in LHS and RHS should be of the same size, 
otherwise the interpreter will throw value error
"""
l = list(range(10))
l[::2] = [i*i for i in range(6,11)] # l = [36, 1, 49, 3, 64, 5, 81, 7, 100, 9]

"""
delete slice of a list
"""
l = list(range(15))
del l[4:10] # l = [0, 1, 2, 3, 10, 11, 12, 13, 14]
del l[::] # l = []
del l[3:] # l = [0, 1, 2]

"""
clear all elements in a list
same as del l[:]
"""
l.clear()

"""
create a shallow copy of a list
same as l[:]
"""
l = list(range(5))
m = l.copy()
m = l[:]


"""
extend this list with another iterable
All of these statements are syntactically valid
"""
l.extend(range(7,10))
l.extend(set({1,2,4}))
l += list(range(3))
l += range(3)
l += set({1,2,4})

"""
update l with its contents repeated n times
if n == 0, l = []
"""
l = list(range(3))
l *= 2 # l =  [0, 1, 2, 0, 1, 2, 0, 1, 2]

"""
insert x at index i
l.insert(i,x)
"""
l.index(2,34)

"""
pop at index i. By default value of i = -1
"""
l.pop(7)

"""
remove first item that is equal to x from the start
throw value error if x is not found
"""
l.remove(8)

"""
reverse a list in place
"""
l.reverse()

"""
End of Functions that mutate a list
"""

"""
Beginning of list Constructors
"""
"""
iterable -> iterable sequence type
sorted produces a sorted list as opposed to reversed which 
produces a reversed iterator
"""
iterable = set()
l = list(iterable)
l = []
l = sorted([4,5,6,6,7])

"""
End of list constructors
"""

"""
Sorting a list in place
"""
l.sort()
l.sort(reverse=True) # sort list in descending
"""
the key corresponding to each item is created once and used for the entire
sorting process. The functools.cmp_to_key() utility is available to convert
a 2.x style cmp function to a key function. sort is a stable sort.
"""
l.sort(key=lambda x: x.prop) # sort according to a property of x

"""

"""










