'''
default dict
1. It is same as dictionary and support all the functions of dictionary but takes first argument as default data type for
   the dictionary.

2. A defaultdict never raise a keyError. Any key does not exist gets the value returned by the default factory.

'''
from collections import defaultdict

y = defaultdict(lambda:0)

print(y[1]) # Since 1 key is not in dictionary y, so it will assign the value to key 1 equals to 0
y[2]= "ram"

print(y)
