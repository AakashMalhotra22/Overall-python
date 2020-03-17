#If you call a module, it will execute all the material in i

from demo1 import add



def fun1():
    add()
    print("From fun1")

def fun2():
    print("From fun2")

def main():
        fun1()
        fun2()

main()