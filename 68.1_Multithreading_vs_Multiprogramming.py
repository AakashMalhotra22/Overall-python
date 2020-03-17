'''
Multi threading vs Multiprocessing:
1. The threads run in the same memory space.
   Processes run in seprate memory space.

2. The threads seems to run parallel but actually they are switching between each other.
   The programs run in true parallel.
'''

#Example
'''
This is an example to show that threads use same memory space but processes run in separate memory.
'''
#Multithreading:
from threading import*
from time import*

y = []

def fun1():
    print("hello1")
    global y
    y.append(1)
    print(y)
    sleep(1)

def fun2():
    print("hello 2")
    global y
    y.append(2)
    print(y)
    sleep(1)
y1 =Thread(target=fun1)
y2 = Thread(target= fun2)

y1.start()
sleep(0.2)
y2.start()

y1.join()
y2.join()
print(y)
'''The output proves that on changing the value in one thread, the value in other thread gets affected.'''


print(" ")
print(" ")

