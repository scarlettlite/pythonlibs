"""
What is mersenne twister
"""
import random

"""
print a random float value in range [0,1)
"""
print(random.random())

"""
print a random integer value in a range [m,n]
"""
print(random.randint(1, 10))

"""
print a random floating point number in [a,b]
"""
print(random.uniform(7.8, 8.9))

"""
pick a random object from a given list of objects
"""
sweets = [
    'oreo',
    'nougat',
    'marshmallow',
    'cottoncandy',
    'toffee',
    'shebertlemon',
    'chocolatefrogs',
    'eclairs',
    'fruittart',
    'walnutbrownie'
]
print([random.choice(sweets) for _ in range(3)])


"""
pick a random list of objects from a list.
add weights so that elements with larger weights are picked up more 
frequently
"""
print(random.choices(sweets,weights=[10,2,3,1,9,6,7,8,4,5], k=3))

"""
shuffle a given a list of objects
"""
random.shuffle(sweets)
print(sweets)

"""
Use Random Module to generate Random data
"""

