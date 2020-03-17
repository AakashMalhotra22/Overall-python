# Why we don't use directly the mathematical function, why we need to write the line from math import* ?

# Answwer: Python has many modules and one of them is for mathematical functions, which are stored in it and you need to write the line
# to call them.

# 1st way

import math

x = math.sqrt(25)
print(x)

y = math.ceil(25.4)
print(y)

print(math.floor(25))
print(math.pow(3,2))

print(math.pi)
print(math.e)

# if you want to use m instead of math, then you need to use the method of allies which states write,
# import math as m instead of import math

import math as m

print(m.sqrt(25))

# Some important lines
'''
1. If you want to import only some functions, write
from math import sqrt,pow
2. If you want to import all the functions, write
from math import * [here * means all]


'''

from math import pow

print(math.pow(25,2))
