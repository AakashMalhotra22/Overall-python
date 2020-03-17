'''
1. Pass by value: In this case if you pass a variable to a function whose value is something and after going through the function if the output of the function does not
   affect the value of the variable then it is pass by value.
   Example:
'''
def update(x):
    x = 8
    print("x",x)

a = 10
update(a)
print("a",a)
'''
Here we are passing a = 10 to update function and the output is 8 but after running the function it is not affecting the value of a which is outside the function as it remains 10
only. This is an example of pass by value.

pass by value means the code should execute like this:
Here a = 10 now this is passed to 
update(a) which means update(a=10)
This means we have passed x =10(not x =a =10 or x = a) in the function which gets updated to give x = 8 without affecting the actual value of a.
This does not mean, we have passed x = a in the function which updates the value of x and a both to give x =8 and a = 8, if this is the case then it is pass by reference. 

Pass by value simply means if you have the variable in the input of the function then that variable will not pass, its value will be passed without affecting the variable.
'''
print("")
print("")
'''
2. Pass by reference: In this case if you pass a variable to a function whose value is something and after going through the function if the output of the function affects
   the value of the variable then it is pass by reference.
   Example:
'''
def update(x):
    x[1] = 0
    print("x",x)

l = [10,1,2,3]
update(l)
print("l",l)
'''
Here we are passing l = [10,1,2,3] to update function and the output is [10,0,2,3] but after running the function it is also affecting the actual value of l which is 
outside the function as its get changed from [10,1,2,3] to [10,0,2,3]).
This is an example of pass by reference.

pass by reference means the code should execute like this:
Here l = [10,1,2,3] now this is passed to 
update(l) which means update(l=[10,1,2,3])
This means we have passed x =l = [10,1,2,3](not x =[10,1,2,3]) in the function which gets updated to give x = a= [10,0,2,3] which also affects the actual value of a.

Pass by reference simply means if you have the variable in the input of the function then that variable will also pass, its value will be also be change with the output.
'''


# Question arises python is pass by value or pass by reference?????

'''
Answer: python is neither supports pass by value nor supports pass by reference it all depends on mutability of the obj type you are passing, if you are passing unmuttable objects
like int, float, str, None, boolean then it would show some properties of pass by value(not full property of pass by value) but if you are passing muttable obj type then it would
show some properties of pass by reference.
'''
print('')
# Consider this example again

def update(x):
    print(id(x))
    x = 8
    print(id(x))
    print("x",x)

a = 10
update(a)
print("a",a)
print(id(a))

# if you consider the id output it shows that before changing the value of x = 8, the id of x = 10 and id of a =10 are same means x and a are saved in same memory or we can
# say that x =a =10, so that means the above example is not completely of pass by value beacuse if it was then the id of x =10 and a= 10 should not be same even before operating.