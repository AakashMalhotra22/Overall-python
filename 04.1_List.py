'''
List:
1. List are the ordered sequence that can hold variety of object types.
2. They used [] brackets and commas to separate objects in the list.
3. They are mutable unlike strings.
4. You can add two list as like this,
Input= [10,1]+[2]
output will be [10,1,2]
5. objects can be retrieved from its index or location.
6. It can be indexed or sliced.

'''
'''Index of list'''
'''
1. Basics- Indexing, slicing.
2. Mutability of list
3. Increment in the list
4. Conversion of string, int, tuples, sets, float, None, dict into the list.
5. Inbuilt functions of list
'''

#1.Basics

nums = [24,12,12,42,32, "aakash", False, "3.2"]
print(nums)# printing the whole list
print(nums[0]) # indexing
print(nums[0:4]) # slicing
print(nums[0:9:2])# slicing application

print(" ")

#2.Mutability of list:

y = ["aakash", "neo", 12, False,2.3]

y[1]= "3" # changing "neo" to "3"
print(y)
y[0:3] = "neo" # in this at index 0, "n" replaces "aakash", at index 1, "e" replaces "neo" and at index 2 "o" replaces 12.print(y)
print(" ")
z = [1,2,3,4,5]
z[0:3] = "neo is fun"
print(z)
#3.Increment of the list:

x = [1,2,3,4,5]
x+=["aakash"]
print(x)

print(" ")

#4. Conversion of string, int, tuples, sets, float, None, dict into the list.

x = "ram"
print(list(x))
x = {1:"ram", 2:"ask"}
print(list(x)) # it will print the list containing the keys of the dict.
print(list(x.values())) #it will print the list containing the values of the dict

y = (1,2,3)
print(list(y)) # it will return the list containing the numbers 1,2 and 3
y = {1,200,3}
print(list(y))# it will return the list containing the numbers 1,200 and 3 but order may be different.

#float, int and None cannot be converted into the list because int, float and None are not iterable.

# One more way to create a list by use of range method

print(list(range(0,9)))





print(" ")














#4. Inbuilt Methods of the list.

'''
Let y be a list
Type-I- These are the functions in which you have to print the list after calling these functions.
Example:
y = [1,2,3]
y.reverse()
print(y)

1. y.extend()
2. y.append()
3. y.clear()
4. y.insert()
5. y.remove()
6. y.reverse() 
7. y.sort()

These are the funcions in which you can call the list directly.
Example:
print(sorted(y))
8. y.pop()
9. y.index()
10. y.count()
11. sorted(y)
12. len(y)
13. min(y)
14. max(y)
'''



x = [3,2,1]
y = ["ram", "aakash"]
x.extend(y)
print(x)

x.append("ramji")
print(x)
x.append("[1,2]") # it will append now [1,2]
print(x)


print(nums.pop(4)) # it wil take out the element from the list whose index is 4.

r = [12, 1 ,14]
print(min(r))

(r.sort())
print(r)

r = [1, 2 ,3]
r.reverse()
print(r)

#Av oid the mistake of None

y = [1,2,6,5]

print(y.sort()) # it will print None because here you are calling the function and not calling the list, so the output is None.

y.clear()
print(y)

z= [1,2,3,4]
z.insert(1,"ram")
print(z)

print(z.remove(1))
print(z)