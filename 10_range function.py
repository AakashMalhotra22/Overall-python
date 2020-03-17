'''
range:
1. It is a function in python and it returns a sequence of numbers, starting from 0(by default) and increament by 1 (by default) and end at specific number.
2. It is repersented by  range()
3. formula range(start,stop,increment)
'''

'''Basics to Advance in range'''

y = range(10)
print(y)

print(list(range(10)))

#formula

print(list(range(10,1,-1)))
print(list(range(10,20,2)))
print(tuple(range(0,10)))
print(2 in range(0,100))