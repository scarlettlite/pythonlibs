"""
ordered, immutable, iterable
only used for integers
range objects represents a sequence , which is different from a list of
integers, which has references to all integers. This means ranges occupy 
less space than lists each range occupies the same(small) amount of memory
range stores start, stop and step , instead 
"""


"""
Operations supported by ranges
1.slicing
2. 'in' and 'not in' : Complexity O(1)
3. len, max, min, 
4. index, count 
"""
s = range(20)
print(s.index(15)) # 15
print(s.count(2)) # 1
print(34 in s) # False
print(range(5) in range(10))

"""
operations not supported by range 
concatenation
"""
try:
    range(3) + range(4)
except:
    print("ranges cannot be concatenated")


"""
Comparisons are sequence based not object based as of 3.3
"""
print(range(0,10,3) == range(0,11,3)) # True (0,3,6,9) == (0,3,6,9)