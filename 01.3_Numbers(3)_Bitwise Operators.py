#There are six types of bitwise operators.
'''
1. Complement(~)
2. And(&)
3. Or(|)
4.XOR(^)
5.Left Shift (<<)
6. Right Shift(>>)
'''

#1. Complement(~) - Tilde

print(~12)
# -13 is the complement of 12 in binary format
# The complement of 1 is 0 and the complement of 0 is 1 in binary format.

'''
To calculate the binary format of the negative decimal number, first find 2's complement = 1's complement + 1 
1's complement is flip of the number 
for example: for 00001000, the 1's complement is 11110111.

The 2's complement is the negative of the decimal number.

Every binary number is represented in 8-bit format.
For example: for 5 - 0101, it will be represented as 00000101
'''

#To show complement of 12 is -13
#LHS - Complement of 12 (00001100) is 11110011

#RHS - The value of -13 is 2's complement.
#First calculate the value of 13 as 00001101
#Then calculate 1's complement as 11110010
# Now calculate 2's complement as 1's complement + 1 = 11110011
# thus LHS= RHS


print(~13)


#2 And(&)
# Same as decimal system, here we use &

print(12&13)
#Here the output is 12.
'''
Because
12 is     00001100
13 is     00001101
Equals to 00001100  [ here 0 means false and 1 is true, so 0 &1 means 0] =12 
'''

#3 Or(|)
# Same as decimal system, here we use |


print(12|13)

#Here the output is 13.
'''
Because
13 is     00001100
13 is     00001101
Equals to 00001101  [ here 0 means false and 1 is true, so 0 | 1 means 0] =13 
'''

print(15|13)

#4 XOR(^)
'''
0 0 - 0 
1 0 - 1
0 1 - 1
1 1 - 0
'''


print(12^13)
# Here answer is 1 because
'''
 00001100
 00001101
^________
 00000001           = 1
'''


#5 Left shift (<<)
#It shifts the number by two decimal places to the left.

print(10<<2)
#This is 40 because
# 10 is 1010.0000, shift two decimals places to the left to get 101000.00 = 40

#6. Right shift(>>)
# It shifts the number by two decimals placees to the right.

print(10>>2)
#This is 2 because
#10o is 1010.0000, shift two decimals places to right to get 10.10000 = 10.000000 =2
