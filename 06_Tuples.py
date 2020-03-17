'''
Tuples
1. Ordered collection of element which contains the different objects types.
2. It can be indexed, sliced but not sorted.
3. If you sort it by use of sorted(y), then it will sort the tuple but the output would be a list.
4. This are immutable, does not support item assignment.
5. It has two inbuilt method
   a. count
   b. index

6. You can use len() also to get the length of the tuple.
7. The benefit of using tuple is that it avoids accidentally changing of the items of the list.
8. It is represented by tuple()
9. tuple can also be written as a = 1,2,3 this is same as a =(1,2,3)
'''

'''
Index
1. Ways to create tuples.
2. Basics of tuples.
'''

print("")
'''Ways to create tuple'''

#1. by comma sepration:
a = 10000,2000,3000
print(a)

print("")

#2. Use of parenthesis

y = (1,2,3)
print(y)

y = ((1,1), (0,0), (-1,-1))
print(y)

print("")
#3. By use of tuple()method.
'''
1. List, string, dict, sets and range can be converted into the tuple.
2. int, float, None and bool cannot be converted into tuple as they are not iterable.
'''

print(tuple([1,2,3]))
print(tuple({4,5,6}))
print(tuple("ram"))
print(tuple(dict(a=2,b =3)))
print(tuple(range(0,10)))

print("")


'''2. Basics of tuple'''

tup = (12, 14 ,15)
print(tup)
print(tup[2]) #indexing
print(tup[0:2]) # slicing
print(tup.count(12)) # count function
print(tup.index(15)) #index function
print(len(tup)) # length function


print(" ")






