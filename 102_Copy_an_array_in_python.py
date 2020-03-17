# Operations
from numpy import*

#1.

arr = array([1,2,3,4,5])

#type-1

arr1 = array( [a+5 for a in arr])
print(arr1)
    
#type-2 operation
arr = arr+5
print(arr)

#Addition of two arrays
r1 = array([1,2,3,4,5])
r2 = array([5,4,3,2,1])

r3 = r1+r2
print(r3)

#Vectorized operations: Certain mathematical operations

print(sin(r3))
print(log(r3))
print(sqrt(r3))
print(max(r3))

#concatenation

print(concatenate([r1,r2]))

#How to copy and add the array

# Way-1
r1 = array([1,2,3,4,5])

r4 = r1

print(r1)
print(r4)

print(id(r1))
print(id(r4))
#In this id are same
print("       ")
#Way-2

r1 = array([1,2,3,4,5])

r4 = r1.view()

print(r1)
print(r4)

print(id(r1))
print(id(r4))

#In this id are different

#There are two different types of copy
#1. Shallow copy: It will copy the array but both the arrays are dependent on each other, if you change the value in one array, the second
#array will also change.

#2. Deep copy: It will copy the array but both the arrays are dependent on each other, if you change the value in one array, the second
#array will remain same.
print("          ")
# Example of shallow copy is:

r1 = array([1,2,3,4,5])

r4 = r1.view()
r1[1]=4
print(r1)
print(r4)

print(id(r1))
print(id(r4))
print("     ")
# example of deep copy

r1 = array([1,2,3,4,5])

r4 = r1.copy()
r1[1]=4
print(r1)
print(r4)

print(id(r1))
print(id(r4))
     
