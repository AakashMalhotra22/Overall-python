'''
zip function:
1. It is opposite of enumerate.
2. It zips together any number of iterables objects together.

'''

'''
Basic to advance
'''
#1

y1 = [1,2,3]
y2 = ['a','b','c']
y3 = [5,6,7,8]
print(list(zip(y1,y2))) # combine to list

print(" ")
print(list(zip(y1,y2,y3)))
#Zip will do the zipping as far as the shortest list.


#2. Advance
y = 1,2,3 # here y represents tuple
print(list(zip(y)))
print("")
#3. Applying for loop in zip

a = (10,20)
b = [30,20]

for item in zip(a,b):
    print(item)
print("")





#4 Zipping two str
a = "ask"
b = 'ram'
print(dict(zip(a,b)))
print(tuple(zip(a,b)))
print(set(zip(a,b)))
print(list(zip(a,b)))
print("")

#5 Zipping two tuple
a = (13,26)
b = (15,25)
print(dict(zip(a,b)))
print(tuple(zip(a,b)))
print(set(zip(a,b)))
print(list(zip(a,b)))

print("")
#6 Zipping two sets
a = {13,26}
b = {15,25}
print(dict(zip(a,b)))
print(tuple(zip(a,b)))
print(set(zip(a,b)))
print(list(zip(a,b)))

print("")
#7 Zipping two dict
a = dict(p = 100, q = 101)
b = dict(s= 51, z = 11)
print(dict(zip(a,b)))
print(tuple(zip(a,b)))
print(set(zip(a,b)))
print(list(zip(a,b)))

print('')
#8 Zipping two lists
a = ["a", "z,", "p"]
b = [0,9,8]
print(dict(zip(a,b)))
print(tuple(zip(a,b)))
print(set(zip(a,b)))
print(list(zip(a,b)))

print('')
#9 Zipping two range
a = range(15,11,-1)
b = range(12,16)
print(dict(zip(a,b)))
print(tuple(zip(a,b)))
print(set(zip(a,b)))
print(list(zip(a,b)))
print("")

