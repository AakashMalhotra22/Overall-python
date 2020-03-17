'''
Method overriding:
1. It is an ability that allows a subclass or child class to provide a specific implementation of a method that is
   already provided by one of its super-classes or parent classes.

2. Method of child class will be given preference.


'''

class A:

    def show(self):
        print("In A show")

class B(A):

    def show(self):
        print("In B show")

a1 =B()
a1.show()
