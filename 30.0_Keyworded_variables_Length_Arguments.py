def person(name, *data):
    print(name)
    print(data) # here data is in form of tuple


person('navin', 28, 'Alwar', 9223924171) #In this, it is not known that what is 28 is it age or something.

# Here we use keyworded variables length argument.

def person(name, **data):# here double star is used to pass multiple data.
    print(name)
    print(data) # here data is in form of dict


person('navin',age = 28, city = 'Alwar', phone_number =  9223924171)

#More easy
print("             ")
def person(name, **data):# here double star is used to pass multiple data.
    print(name)
    for i, j in data.items():
        print(i,j)


person('navin',age = 28, city = 'Alwar', phone_number =  9223924171)