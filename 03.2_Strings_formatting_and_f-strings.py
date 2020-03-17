 dictn = {"name": "Tanu", "age":18}
dictm = {"sex": "female", "height": "157cm"}
                                                                   # For dictionary

'''String Formatting'''

# 1st way
print("My name is {} and my age is {}".format(dictn['name'], dictn["age"]))

# 2nd way
print("My age is {1} and my name is {0}".format(dictn['name'], dictn["age"]))


# 3rd way
print("My name is {0[name]} and my age is {0[age]}".format(dictn))

# 4th way
print("My name is {0[name]} and my age is {1[age]}".format(dictn, dictn))

# 5th way
print("My name is {0[name]} and my height is {1[height]}".format(dictn,dictm))

#6th way
print("My name is {0[name]} and my height is {1[height]}".format(dictn,dictm))


'''f- string'''

print("                                                     ")

# 1st way
print(f"My name is {dictn['name']} and my age is {dictn['age']}")

print("                  ")
                                                                        #For list


lst = ["Aakash", 1, "Malhotra"]
lsty = ["Tanu",1 ,"Ahuja"]

'''String formatting'''

# 1st way
print("Hello, my first name is {} and last name is {}.".format(lst[0], lst[2]))
# 2nd way
print("Hello, my first name is {0[0]} and last name is {0[2]}.".format(lst))
# 3rd way
print("Hello, my first name is {0[0]} and last name is {1[2]}.".format(lst, lsty))

'''f- strings'''
print(" ")
print(f"Hello, my first name is {lst[0]} and last name is {lst[2]}.")

print("                                          ")

                                                                         # For keywords and For strings
my_name = "ram"
my_age = 18

'''String formatting'''
# For keywords

print("This is {} of age {}".format("aakash", 18))
print("This is {name} of age {age}".format(name = "aakash", age= 18))

# For variables

print("This is {} of age {}".format(my_name, my_age))
print("This is  of age {1} and name {0}.".format(my_name, my_age))

'''f-string'''
print("  ")

print(f"This is {my_name} of age {my_age}")




                                                                  # float formatting

# Formula for float formatting {value:width,.precisionf}
'''String formatting'''

print("{:2,.2f}".format(100000))
print("{:19,.2f}".format(100000))
print("{:019,.2f}".format(100000))
print("{:05,.2f}".format(9))
print("{:2,.2f}".format(9.213213211))

print("  ")
