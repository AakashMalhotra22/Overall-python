'''
Different ways to call a function
'''

#1
def greet(a):
    print(a,"hi")

y = greet
y(3)

#2 Passing a function in another function

def nam(a):
    def greet(b):
        print(a,"hello",b)
    return greet #here you are not writing parenthesis,so you have to write it outside at the time of calling.

nam(2)(3)#Here 2 parameter is passed to nam function and 3 parameter is passed to greet function

'''___________OR__________'''

y = nam(2)# Here 2 is passed to nam function
y(3) #here 3 is passed to greet function
