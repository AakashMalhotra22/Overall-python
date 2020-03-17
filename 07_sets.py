'''
Sets:
1. These are the unordered collections of the unique elements.
2. In the output no element will repeat more than once.
3. The order of the set in the output may not be same as the order of the set in the input.
4. 'set' are not subscriptable which means it does not support indexing and slicing
5. It is represented by set()
6. It is immutable
'''

'''
1. Basics
2. Ways to create sets object.
3. Inbuilt methods in sets.
'''

'''Basics'''
#set uses the concept of hash which means it will fetch the elements as fast as possible no matter which is coming first or last.
#That's why you donot get the values of the sets in the output in the same sequence as in the input.
print("")

s = {22, 25, 9, 98}
print(s)
s = {1,2,3,3}
print(len(s)) # here length of the s is 3 not 4 as 3 repeats two times.
print("")
# Adding element in sets

s = {1,2,3, "a", 2.3}
s.add(10)
print(s)
print('')

'''Ways to create sets.'''
#Ist way by use of parentheses.

s = {1, False, True, 2.3,  "ask"} # as 1 = True, so it has removed True in ouput
print(s)

# 2nd way by use of set()
'''
1. List, tuple, dict, string and range can be converted into sets objects.
2. int, float, None and bool cannot be converted into the sets objects.
'''

print("")

print(set([1,2,3]))
print(set("ask"))
print(set(range(0,9)))
print(set((1,2,3)))
print(set(dict(a=2,b=3)))
print(" ")


# Methods in sets.
'''
1. a1.add(2)
2. a1.clear()
3. a1.copy(a2)
4. a1.difference(a2)
5. a1.difference_update(a2) it will change the value of a1 to the output obtained by a1.difference(a2).
6. a1.discard(value)
7. a1.intersection(a2)
8. a1.intersection_update(a2) it will change the value of a1 to the output obtained by a1.intersection(a2).
9. a1.issubset(a2)
10. a1.issuperset(a2)
11. a1.isdisjoint(a2)
12. a1.symmetric_difference(a2) opposite of difference
13. a1.symmetric_update(a2) it will change the value of a1 to the output obtained by a1.symmetric_difference(a2).
14. a1.union(a2)
15. a1.update(a2) update with the union.
'''


s = {1,2,3}

s.add(1) # add method
print(s)

s.clear() # clear method, clears the set.
print(s)

print("")
r = {1,2,3}
sc = r.copy() # copy the r in sc.
print(sc)
# if you change anything to r then it would not affect sc.

r.add(4)
print(r)
print(sc)

print("")

# difference method
a = {1,2,3}
b = {1,5,6}
print(a.difference(b))
print("")
# difference update method: It returns the elements of set1 by removing the element of set2 in it.

s1 = {11,12,13}
s2 = {11, 3,4}
(s1.difference_update(s2))
print(s1)
print("")

# discard function

a = {1,2,3}
a.discard(2) # discard 2 from the set
print(a)
print("")
#intersection method

a = {1,2,3,4}
b = {1,2,4}

print(a.intersection(b)) # print out the element of a which are also in b.

print("")

#intersection update

a = {1,2,3,4}
b = {1,2,4}
a.intersection_update(b) # it will update the value of a to intersection of a and b.
print(a)

print("")

#is disjoint

a1 = {1,2,3}
a2 = {1,5,6}
a3 ={10}

print(a1.isdisjoint(a2))# it will return true if a1 and a2 have no elements in common.
print(a1.isdisjoint(a3))

print("")

#issubset and issuperset

a1 = {1,2,3}
a2 = {1,2}

print(a2.issubset(a1))# it will return true or false if a2 is subset of a1.
print(a1.issuperset(a2))

print(" ")


#symmetric difference

a1 = {1,2,3}
a2 = {1,2}

print(a1.symmetric_difference(a2)) # it is opposite of difference
print("")

# union
a1 = {1,2,3}
a2 = {5,6,7}
print(a1.union(a2))
(a1.update(a2)) # it will update the value of a1 to as in the last operation
print(a1)