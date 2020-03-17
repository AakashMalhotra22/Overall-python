person = {"name": "aakash", "age": 23}

sentence = "My name is {} and my age is {}".format(person["name"],person["age"])
print(sentence)

# another way of above

sentence = "My name is {1} and my age is {0}".format(person["name"],person["age"])# use of 1 indicates that it uses second part of format
# for 1 and first part for 0 of format
print(sentence)

# another way of above


sentence = "My name is {0[name]} and my age is {1[age]}".format(person,person) # here 0 before name is that name is taken from first
# part of format and #1 before age means age is taken from second part of format.

print(sentence)

# If both the values are from same dictionary

sentence = "My name is {0[name]} and my age is {0[age]}".format(person)

print(sentence)

print("         ")
'''
for classes
'''


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person("ram", 13)

y = "his name is {} and his age is {}".format(p1.name,p1.age)
print(y)

# 2nd way

y = "his name is {0.name} and his age is {0.age}".format(p1)
print(y)


'''
3. keworded arguments
'''

y = "Hello you are {name}, right".format(name= "pappu")
print(y)

print(" ")
'''
4 kwargs

'''
p = {"name": "pinki", "age":12}
y = "Hello you are {name} and your age is {age}.".format(**p)
print(y)



print("   ")
# 5 for loops

'''First'''
for i in range(1,11):
    print("The value is {}".format(i))

'''If you want to do some changes'''

for i in range(1,11):
    print("The value is {:02}".format(i))

print("")
# 6 decimal places


pi = 3.141592
y = "pi is {:.2f}".format(pi)
print(y)

#7. Comma sperators for large values
y = "1MB is equals to {:,.2f}".format(1000**2)# here , is for comma seprators and .2f is 2 floating values are required.
print(y)

print(" ")
#8. List

d = [1,2,3]

print("ram {0[0]},{0[1]},{0[2]} go !".format(d))

print("   ")
#9. formatting date and time

import datetime

my_date = datetime.datetime(2016,9,24,12,30,45)


print("The date is {:%B, %d, %Y}".format(my_date))

print("{0:%B, %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year".format(my_date))