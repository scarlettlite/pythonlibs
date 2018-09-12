"""
Truth Value testing
Each object can evaluate to True or False. depending on either __bool__() or __len__()
If a sequence has length zero it evaluates to False
x and y : x if x is false else y
x or y : x if x is true else y
"""

"""
Comparison Operators
There are 8 operators in total
1) <
2) >
3) <=
4) >=
5) ==
6) !=
7) is
8) is not

All have equal priority. Can be arbitrarily chained together
x <= y < z != a
Will return false as soon as one of the conditions return false. Expression will not 
be evaulated further
Objects can define dunders : __lt__, __eq__, __gt__, __le__, __ge__.
In practice __lt__ and __eq__ are enough

Behavior of is and is not cannot be customized
"""

"""
how do compare functions work
how to write compare functions for descending and ascending
"""



#