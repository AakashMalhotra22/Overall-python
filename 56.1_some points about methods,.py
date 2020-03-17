#Point 1: If there are more than one method in a class with same name then the method which comes at the last will be given preference.
#          It does not matters whether the method is instance, class or static.
#          It does not supports method overloading.5


class student():
    school = "Aakash" # This is class variable

    @classmethod # This is required decorators before the class method.
    def info(cls):# For class method, use cls instead of self.
        return cls.school
    def info(self,a):
        print(a)
    def info(self,b):
        print(b+2)
    @staticmethod
    def info():
        print("hello")

s1 = student()
print(s1.school)
s1.info()