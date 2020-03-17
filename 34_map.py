'''
map:
1. syntax
   map(function_name,iterator)

2. It iterates through each value of the iterator and pass that value to the function and pass the modified values which is obtained from the function to map function from where
   you can print it out the value
   for example if we have function f1 and iterator [a,b,c,d] then it would just give you this f1[a], f1[b], f1[c], f1[d]
'''

'''
Examples from basic to advance:
'''
#Example1:
n = [0,1,2,3,4,5]
# Way-1
doubles = list(map(lambda n: n*2, n))
print(doubles)

# Way-2
doubles = (map(lambda n: n*2, n))

for i in doubles:
    print(i)

print("")

#Example-2

square = list(map(lambda a:a*a,n))
print(square)

#Example-3
j = " 123213  2132321 22321321 2321321321     "

y = list(map(int, j.strip().split())) # converts the str by applying operation into list of integers.
print(y)

'''
In above function, .strip() is used to remove extra spaces between str j
.split() is used to convert the string into list of str.
int is used to convert list of str into list of int
'''

#Example- 4
y = list(map(float, [1,2,3]))
print(y)