#Example 1:
class Computer:
    def __init__(self, ram, rom):
        self.ram = ram
        self. rom = rom


c1 = Computer(4,16)
print(c1.ram)
c1.ram = 45 # Attributes of the class support muttability
print(c1.ram)

#You can create new attributes also like this
c1.ask = "aakash"
print(c1.ask)


print("")
# Example 2:
class Computer:
    def __init__(self, ram, rom):
        self.ram = ram
        self. rom = rom
    def add(self,a,b):
        print(self. ram +a+b)
    #In this class you can use self.ram, self.rom variable anywhere in any function but you cannot use this a,b function in other function, for example:
    def sub(self):
       '''
        print(a-b)# It is not recognising the variables of the add function outside the add function.
        print(self.a,self.b) # it will give an error that computer object has not attribute a and b.
        '''

c1= Computer(3,16)
c1.add(3,4)
c1.sub()
print("")