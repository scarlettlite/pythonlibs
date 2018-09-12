#convert a number into a binanry string
print(bin(677)) #0b1010100101

#convert a decimal number into a binary string without '0b' prefix
print(format(677, 'b'))

#convert a value of true or false
print(bool(678))

def breakpoint():
    pass
#drop a debugging point in the code, available in 3.8
print(breakpoint())

"""
bytesarray : a mutable array of integer values between [0,255]
"""
"""
bytes: an immutable array of integer values between [0,255]
"""

print(chr(90)) # return a string which represents a character whose unicode code point is represented by that integer
print(complex(2,3))
print(complex('1+7j'))

obj = {'name':'eragon'}
#delattr(obj, 'name') # equivalent to del obj['name']

#return the names in current local scope or names of properties of an object
#if an object is passed to it
dir()

#enumerate objects in an iterable with the index values starting at 'start'
#doesnt mean the for loop will start from the 'Start'th' object of the iterable
print([(i,x) for i,x in enumerate(range(5), 5)])

#evaluate a python expression, with globals and locals. globals must be a python 
#dictionary and locals can be any maping type
eval('4+1') 

#exec(object, globals, locals). execute object as python code, object may be string or a code
#objects
exec('5+1')

#globals() to get the current dictionary of globals
#locals() to get the current dictionar

#Construct an iterator with elements in iterable that returns true for function
#filter(function, iterable) 
#for creating a filtered list use list comprehension
#use itertools.filterfalse() returns an iterator over elements which return false for function


#Class frozentset() : create frozenset

#getattr(obj, attrributename) : get the value of the named attribute 

#globals() return a dictionary rrepresenting the current global symbol table

#hasattr(object, name)

#return a unique integer which is the hash value for the object
#hash is deteremined by the value of the object and not the type
#for example 1 and 1.0 have the same hash value
print(hash('Shivani'))


#help([object]). Invoke builtin help system
#if a string is passed then look for that string in the documentation

#return a string which gives the hexadecimal representation of the number
print(hex(78)) #0x4e
print(format(78,'#x'))#0x4e
print(format(78,'x'))#4e
print(format(78,'#X'))#X4E
print(format(78,'X'))#4E

#return an integer that is guaranteeed to be unique and constant during its lifetime
#two objects may have the same id with non overlapping lifetimes
id(89)

#input
#if the prompt argument is present it is written to the standard output
#without a traling newline

#class int
#convert a string to integer. 
print(int('20'))
#convert binary string to integer
print(int('1010110', 2))
#convert octal string to decimal integer
print(int('567', 8))
#convert hexadecimal string to decimal integer
print(int('6ab', 16))

#isinstance(obj, classinfo)
#return true if the object argument is an instance of the classinfo
#argument or of a (direct, subdirect or virtual) subclass thereof
#classinfo can also be a tuple of objects. In that case isinstance works like any

#issubclass(class, classinfo) return true if class is a subclass of classinfo or
#an direct, indirect and virtual classes. classinfo can also be a tuple of class objects

#iter(object, [sentinel])
#return an iterator object . object should adhere to iterator protocol(__iter__)
#or sequence protocol(__getitem__()) difference between a sequence and interator
#is that a sequence is ordrered. if object is an object and sentinel is passed 
#raise a stop iteration exception when object returns a sentinel

#return an iterator that applies function to every
#item of iterable yielding the results. Can pass more than one iterable
#will exhaust when one of the iterables exhaust
#map(function, iterable1, iterable2, ...)

#max(iterable, key, default)
#key here works like key in list.sort(). if iterable is empty
#return the default value

#min(iterable, key, default)
#same as max

#next(iterator, default)
#return the next item in the iterator by calling the next 
#dunder

#class object. return a new featureless object. it has methods that are common to all instances of Python classes

#return an octal string representation  
print(oct(890))#0o1572

#open(file, mode='r', encoding=None, buffering=-1, newline=None, opener=None, closefd=true)
#mode = read,write,append,binary,text
#encoding = if None then getpreferredencoding(false) is called to return local encoding
#encodings available in codecs python module can be used here
#buffering: for binary files devices block size is used which is typically 4096 or 8192 bytes
#for text files, lines are buffered . if buffering > 1. It indicates fixed size bytes buffer 
#newline : separate behavior for instream and outstream, values = None. '\n','\r','\r\n'
#closefd : for filename this should always be true. Only relevant when file argument is a file descriptor
#opener: callable that returns an open file descriptor


#ord(): opposite of chr(). Given a character , return the integer representation of the unicode point of that character
#pow(x,y[,z]): if z is given, x must be an integer and y should be positive. otherwise x and y can have floating values as well


#print(*objects, sep=' ', end='\n', flush='false', file=sys.out)
#for printing in the same line sep = ' ' and end=''. 

#class property(fget=None, fset=None, fdel=None, doc=None)

#reversed: object must implement __reveresed__(). or should implement sequence protocol
#__len__(), __getitem__()

#round(number[,ndigits=0]) #round off number to precision ndigits after decimal

#class slice: used by numerical python in same places

#sorted: use functools.cmp_to_key() to convert a compare function to key function
#it provides a stable sort











