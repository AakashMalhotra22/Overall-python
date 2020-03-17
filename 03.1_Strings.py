'''
Strings: These are the ordered sequences which means you can use indexing and slicing to grab values.
         It is a collection of characters and you can use single and double quote to write strings.
'''
'''Properties of strings'''
'''
1. strings doesn't support item assignment.
   Example y ="112"
   here at index position 0 there is 1 and you want to change it to 3, then you cannot apply the operation y[0]=3, it will show an error.
   
2. strings are immutable, means you cannot do item assignment.
'''

#Index
'''
1. Basics of strings- raw strings, escape sequence.
2. Indexing and Slicing in Strings.
3. String concatenation
4. In-built method in strings.
5. Operators in strings.
'''

'''1. Basics of strings:'''

print("navin")
print('navin')

#Backslash can be used for writting single and double quotes in strings.

print('navin\' ')
print('navin\'s "laptop"')

print(10*"navin")

# how to write backslash in python

print("2\\2")

# Escape sequence:

print("ram is \n good") # It will take good in the next line
print("ram is \t good") # it will provide big space between is and good.

# raw strings: It would nullify the effect of the escape sequences on the strings.
print(r"ram is \n good")
print(r'c:\docs\navin')

print("     ")
print("     ")


'''2.Indexing and Slicing in Strings.'''
# Indexing:
''' 
 1. Indexing uses [] notation after string.
 2. Indexing allows you to grab a single character from the string.
 3. Indexing Starts from 0.
'''

name = "youtube"
print(name[4])
print(name[0])
print(name[-1])
print(name[-2])
ram = "ask"+name[4]
print(ram)


#Slicing:
'''
1. It allows you to grab a subsection of multiple characters of the string.
2. It has following syntax.
   [start:stop:step]
   a. start is a numerical index for the slice start.
   b. stop is the index you will go up to (but not include)
   c. Step is the size of the "jump" you take.
'''

y = "rameshwar"

print(y[:3:])#start from 0 index till index 2 with default jump of 1.
print(y[1:3]) # start from index 1 till index 2 with default jump of 1.
print(y[1:7:2])# start from index 1 till index and go till index 7 with jump of 2.
print(y[::-1]) # reverse the string, it starts from the last letter of string and go in reverse direction.

print("     ")
print("     ")

'''3. String concatenation'''

y = "ram"
y1 = "youtube"

print(y+y1) # it will add both the string
print(y,y1)
print(y+y1[3:])

'''
You can concatenate the strings by two ways, first way is by use of + and second way by use of ,(comma)
The difference is comma produces an extra space while + does not produce an extra space.
This can cause problem while making pattern.
'''

print("   ")
print("   ")


'''
4. In built methods in list:
1. len()
2. split()
3. partition()
3. upper()
4. isupper()
5. islower()
6. capitalize()
7. count()
8. find()
9. center()
10. strip()
11. rstrip()
12. lstrip()
'''

y = "ram is"
print(y.capitalize()) # capitalize the first letter of the string or phrase.
print(y.upper()) # Make the whole string in uppercase.
print(y.isupper()) # check whether the sting is upper or not if it is upper then return True else False.
print(y.lower()) # Make the whole string in lowercase.
print(y.islower()) # check whether the sting is lower or not if it is upper then return True else False.
print(len(y)) # print the length of the string.


print("")
y = "hiihhihihihhi"
print(y.split())# split the string and convert into the list and the splitting takes place through space, space is the default value.
print(y.split("i")) # here the splitting takes place from "i"
print(y.partition("i")) # partition the string through i .

'''
split method splits the string at every instance of the character.
partiion method splits the string a the first instace of the charcter and the character through which the string is partitioned comes in between.
'''

print(" ")
x = "iram fine"
print(x.count("i"))# count the numbers of "i" in the string.
print(x.find("i")) # return the index position of i, since first i comes at 0, so return 0.
print(x.center(20,"z")) # it will fit the string x between some "z" with length of the string is 20.

print(" ")

# strip() function
y = "aaaaaaaaaaramaaaaaaaaaaa"
print(y.strip('a')) #remove extra a
y = "       ram      "
print(y.strip()) # remove extra space, it is the default value

k = "aaaaramaaaa"
print(k.rstrip(('a')))# remove extra a from the right.
print(k.lstrip('a')) # remove extra a from the left.

j = "aaaramaaaramaaaa"
print(j.strip("a"))

print("")
'''Operators in strings.'''
x = "ram"
print(x[-1]=="m") # it will return True if last character is "m









