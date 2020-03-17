# Matrices
# Multi- dimensional array:

from numpy import*

arr1 = array([
    [1,2,3,4,5,6],
    [7,8,9,10,11,12]
])

print(arr1)
print(arr1.dtype) # gives type of array
print(arr1.ndim)# gives dimension
print(arr1.shape) # it tells the number of rows and column.
print(arr1.size) # it will tell you the size of entire block.


#Conversion of two dimension array in one dimension.
arr2 = arr1.flatten()
print(arr2)

#Conversion of one dimension into other dimension
arr3 = arr2.reshape(2,6 )
print(arr3)

arr4 = arr2.reshape(2,2,3)

print(arr4)


m1 = matrix(arr3)

print(m1)

m2 = matrix('1 2 4; 3 4 7; 9 5 6')
print(m2)

m3 = matrix('9 8 7; 6 5 4 ; 3 2 1')
print(m3)

m4 = m3 + m2

print(m4)

m5 = m3*m2
print(m5)