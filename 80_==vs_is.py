'''
== vs is
1. The == operator compares the values of both the operands and checks for value equality.
1. is operator checks whether both the operands refer to the same object or not.

2. When you want to do comparison on the basis of values, then use == operator.
2. When you want to do comparison on the basis of object type also, along with values, then use is operator.
'''

#1

y1 = []
y2 =[]
y3 =y1
print(y1 ==y2)# output is True because the value of y1 is same as value of y2
print(y1 is y2)# output is False because the y1 is different object and stored in different memory and y2 is different object and stored in different memory.
print(y1 is y3)# output is True because y1 and y2 are pointing to the same objects

print(*'\n')
#2

print(2.0==2)# Since, the value of 2.0 is same as 2, thus the output is true.
print(2.0 is 2)# Since, the 2.0 is float object and 2 is int object, thus output is False.


