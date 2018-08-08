"""
Immutable, ordered, iterable sequences
provides an implementation for hash
"""

"""
tuple constructors
iterable => iterable type
if iterable is already a tuple it is 
returned unchanged
its the comma that creates a tuple. 
Brackets are not necessary to 
create tuple . Parentheses are only required 
remove ambiguity in cases such as an empty tuple
"""
iterable = []
t = ()
t = (1,) # tuple with one element
t = 1,3,4
t = (1) # here t will of type int
t = tuple(iterable)

"""
Common operations on tuples
"""
1 in (1,2,3,4) # 1 in 1,2,3,4 will throw a syntax error
2 not in (1,3,4,5)

"""
Concatenation 
"""
s = 1, + 2,3
s = (1,) * 3
s = 3 * (2,3)
s = (1) + (2) # these are numbers not tuples
s = 3 * 3, 3 # s = 9,3 , this might be because * has higher priority than ,
print(s)


"""
slicing
"""
t = tuple(range(10))
print(t[7:9])
print(t[7::-1])
print(t[::2])


"""
length, min, max
"""
print(len(t))
print(min(t))
print(max(t))



"""
find index of element in t
will throw a value error if the element
is not found
"""
t.index(8)


"""
return count of x in tuple t
"""
t.count(6)











#print((1,3) + (2,4)) # 