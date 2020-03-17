'''
Operator Overloading:

1. Operator Overloading means giving extended meaning beyond their predefined operational meaning.
   For example:
      + operator has predefined operational meaning of adding two numbers like 2+3 = 5

      a) But in case of str it just joins two strings,
      b) In case of list, it just merge two lists
      c) in case of int, it just adds two numbers
      This happens because + operator is overloaded by str class, int class and list class.
      In all of these classes, extended meaning of + operator is defined by use of the special method __add__()

   In the same way, you can create your own class in which you can define your own meaning of + operator by overloading the
   + operator in your class by use of special method __add__().
   After this you can also perform the operation like print(s1+s2) where s1 and s2 are objects of your class.



2. You have noticed that the same built-in opertor or function shows different behavior for objects of different classes, this is because operator overloading.

3. Some of the python special methods.

               Binary Operators                                       Comparision Operators
        Operator             Special Method                    Operator               Special Method
  1       +               __add__(self,other)                    <                  __lt__(self,other)
  2       -               __sub__(self,other)                    >                  __gt__(self,other)
  3       *               __mul__(self,other)                    <=                 __le__(self,other)
  4       /               __truediv__(self,other)                >=                 __ge__(self,other)
  5       //              __floordiv__(self,other)               ==                 __eq__(self,other)
  6       %               __mod__(self,other)                    !=                 __ne__(self,other)
  7       **              __pow__(self,other)


             Assignment Operators                                       Unary Operators
        Operator              Special Method                    Operator               Special Method
  1       -=               __iadd__(self,other)                    -                  __neg__(self,other)
  2       +=               __isub__(self,other)                    +                  __pos__(self,other)
  3       *=               __imul__(self,other)                    ~                  __invert__(self,other)
  4       /=               __idiv__(self,other)                           For print statement
  5       //=              __ifloordiv__(self,other)           Operator                 Special Method
  6       %=               __imod__(self,other)                 print(object_name)     __str__(self)
  7       **=              __ipow__(self,other)






Faq's

1. How the operator works in python????

   When any of the operations such as addition, subtraction or any other is done, then it simply means we are calling method.
   for example:
   2+3
   gives you 5
   but behind the scenes it simply not happened.
   behind the scenes it converts 2+3 in the method
   init.__add___(2,3)

2. Why + operator works in case of two number but not in case of your defined class objects?

   whenever you use add symbol between two numbers it first converts it into above method init.__add__(a,b) then solve it, but in case of
   objects and classes, this symbols like +,- and many other cannot be used, for this you have to defined these methods in their classes.
   for example here you are adding 2 and 3, where 2 and 3 are objects of in built class int where + operator is already defined but in case of two
   objects of your defined class + operator is not defined for that you have to define + operator in your class.

3. Why print statement works in case of int, str, list and so on to print what you have written but not in case of your object and classes like print(s1) where s1 is object of
   your defined student class???

   Consider,
   a = '9'
   print(a)
   here a is an object of string, so when you write print(a), it calls the method (a.__str__()), this method returns the value of a to  print 9.
   Now in case of object s1 which belongs to the class student when you write print(s1), it first checks is there any method __str__ (), if there is then it just acts
   according to what is returned in the method.
   But in case if there is no method __str__(), then it just prints out its class name and its location.

   In case of string, it is an in built class where if you write print('9') it will print '9' as there is __str__ function defined in it.
   but in case of the class which you have defined if you call its object like print(s1) then it will print only its class name and
   location as you have not defined in it like as defined in inbuilt class string.
   So you have to defined in it.
'''

'''
Consider the examples:
'''

# Example 1:

class student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        return student(m1,m2)


    def __gt__(self, other):
         m1 =self.m1 + self.m2
         m2 = other.m1 + other.m2
         if m1 > m2:
            return True
         else:
            return False

    def __str__(self):
        return'{} {}'.format(self.m1, self.m2)


s1 = student(23, 34)
s2 = student(32, 37)

print(s1)
print(s2)

print(s1+s2)

student1 = s1 + s2 # This add sign means that Student.__add__(s1,s2)
print(student1.m1)

print(s1>s2)


if s1>s2:
    print("s1 is good")
else:
    print("s1 is not good")

print(s1)
