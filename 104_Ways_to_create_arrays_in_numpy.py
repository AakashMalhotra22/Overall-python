from numpy import*
# Different ways to create an an array:

'''
1.array()
2. linspace()
3. logspace()
4.arange()
5.zeros()
6. ones()
'''

#1. array()

arr = array([1,2,3,4,5])
print(arr)
print(arr.dtype)

#In array there can only be same type of elements, so if you write both float and int then it will convert all the values into float.

arr1 = array([1,2,3,4,5.0])
print(arr1)
print(arr1.dtype)
# You can also tell that to which type the values should be converted.

arr1 = array([1,2,3,4,5.0],int)
print(arr1)
print(arr1.dtype)

arr1 = array([1,2,3,4,5.0],float)
print(arr1)
print(arr1.dtype)

print("                     ")
print("                       ")
#2. linspace()

arr = linspace(0,16,4)

print(arr)
#If you not specify the number of parts, then it will take 50 elements as default.

print("               ")
print("               ")
#3. arange()- it is not arrange, it is a range.

arr = arange(1, 15, 2)
print(arr)
# In case of linspace, it is number of parts, in how many parts should we divide
# In case of arange, it is number of steps, like the common difference of AP.

print("               ")
print("               ")

#4.logspace()
''' In this spacing depends two numbers depends upon log of it, in the next example it will start from 10 rase to power 1 to 10 rase to 
power 40 and divide them into 5 parts.
'''

arr = logspace(1,40,5)
print(arr)

# if you don't want to print in terms of e, then,

print('%.2f'%arr[0]) # this gives the first element 10 raise to power 1 that is 10 in terms of numbers.
print('%.2f'%arr[4])

print("               ")
print("               ")

#5. zeros()
#It will makes all the elements zero.
arr = zeros(5)
print(arr)

print("               ")
print("               ")

#5. ones()
#It will makes all the elements ones.

arr = ones(5)
print(arr)

#If you want to convert it into int, you can also do so.

arr = ones(5,int)
print(arr)
