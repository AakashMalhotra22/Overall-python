class operation:
    def __init__(self,a,b,arg1,arg2):
        self.a = a
        self.b = b
        self.c = self.addition(a, arg2)

    class addition:
        def __init__(self,arg1,arg2):
            self.n1 = arg1
            self.n2 = arg2
        def sum(self):
            print(self.n1+self.n2)

'''
In case when inner class takes argument and you want to create the object of inner inside the outer class, then you have to pass the parameters of the inner class object 
in the outer class object.
'''
# Way -1
y1 = operation(3,4 ,10,10)
print(y1.c.n1)
y1.c.sum()

print("")
#Way-2
y1 = operation(3,4,10,10)
print(y1.addition(2,3).n1)
y1.addition(2,3).sum()

print("")

#Way-3
y1 = operation(3,4,10,10)
c1 = y1.c
print(c1.n1)
c1.sum()

print("")

# Way-4
y1 = operation(3,4,10,10)
c1 = y1.addition(2,3)
print(c1.n1)
c1.sum()

print("")

# Way-5
y1 = operation.addition(3,4)
print(y1.n1)
y1.sum()
