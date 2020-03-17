#MultiProcessing:
'''
This is an example to show that processes use separate memory space.
'''

from multiprocessing import*
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

if __name__=="__main__":
    y1 =Process(target=fun1)
    y2 = Process(target= fun2)

    y1.start()
    sleep(0.2)
    y2.start()

    y1.join()
    y2.join()

    print(y)
'''The output proves that on changing the value in one process, the value in other process does not gets affected.
   The value of y does not get affected.
'''

