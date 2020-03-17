class C:
    count = 0

    def __init__(self,a):
        self.count+=1 # self.<something> stands for object variable not for the class variable, so that's why the output doesnot affected.
        self.a = a

y = [C(i) for i in range(10)]
print(C.count)

'''
Reason2:
when we expect a variable in a class to be consistent across instances\objects, we define at class level.
Here count is a class variable which is consistent across all its instances or objects.
'''

print("")
'''Example 2'''


class C:
    count = 0

    def __init__(self, a):
        C.count+=1 #Here now count is stored as the static variable.
        self.a = a


y = [C(i) for i in range(10)]
print(C.count)


print("")

'''Example 3'''

class C:
    count = 0

    def __init__(self, a):
        self.a = a
        C.count+=1
    def start(self):
        print(f"self.count is {self.count} and C.count is {C.count}")

y = C(3)
print(y.count)
print(C.count)
y.start()

print("")
#Example 4

print("")

class C:
    count = 0

    def __init__(self, a):
        C.count+=1 #Here now count is stored as the static variable.
        self.a = a
    def start(self):
        print(f"self.count is {self.count} and C.count is {C.count}")


y = [C(i) for i in range(10)]
print(C.count)
C.start(y)
print('')
x = C(1)
print(C.count)
C.start(x)