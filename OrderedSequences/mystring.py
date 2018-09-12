"""
String -str
immutable, ordered, iterable
"""
"""
'in' can be used to check if a substring is in a string .Complexity : O(n)
if two strings are only separated by space then they are concatenated together
'in ' 'the' == 'in the'
when called on user defined objects str will return object.__str__(). If __str__
is not defined it fallbacks to repr
"""

"""
Strings provide two types of formatting one is based on the format method and the 
other one is based on printf style of formatting. The latter handles a narrower range of 
type and difficult to get right , but is faster than the format method
"""

"""
Repetetive Concatenation for immutable types has complexity in quadratic.
Instead construct a list of strings and once you are done constructing a list
concatenate using join
"""

"""
rindex only exists for strings not for lists
"""

"""
Beginning of functions for strings
"""
s = "a string"

"""
capiltalize the first character of the string
"""
s.capitalize()

"""
return a centered string with the given width and fill empty space with fillchar
return original string if width is less than the length of the string
can be used for formatting
"""
s.center(20, '$')

"""
return the count of non-overlapping substrings. Complexity is O(length of string)
avoid using it because most cases will involve overlapping strings
"""
'hahahaha'.count('haha')#returns 2 , even though 'haha' occurs twice here


"""
return True if the suffix is found. Suffix can also be a tuple od suffixes
Optional start and stop arguments can also be given
"""
s.endswith(('yu','89'))

"""
replace each tab with number of spaces passed to the function
"""
s.expandtabs(4)


"""
find the first of index of the substring from the beginning.
if there is failure return -1. Does not throw any errors. use this
instead of index which throws an value error
"""
s.find('i')

"""
find the first index of a substring from last. return -1 if the substr is not 
found. Does not throw value error
"""
s.rfind('i')


"""
like find and rfind, but raise a value error if the substring is not found. Avoid using this
"""
s.index('i')
s.rindex('i')


"""
return whether the string is alphanumeric
"""
s.isalnum()


"""
return whether a string is alphabetical
"""
s.isalpha()


"""
return whether is a string comprised of ascii characters
new in version 3.7
"""
#s.isascii()


"""
whether the string is a decimal. Number consists of 0-9
and .
"""
s.isdecimal()


"""
superset of s.isdigit(). includes superscripts, substripts etc
"""
s.isdigit()


"""
is the string a valid identifier according to the rules of language
"""
s.isidentifier()

"""
"""

"""
End of functions for strings
"""