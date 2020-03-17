from threading import*
from time import *
start = perf_counter()# This is a time counter

def ram():
    for i in range(5):
        print("hello")
        sleep(1)

def ji():
    for i in range(5):
        print("ji")
        sleep(1)

y1 = Thread(target =ram)
y2 = Thread(target =ji)
y1.start()
sleep(0.2)
y2.start()

y1.join()
y2.join()

finish = perf_counter() #This is time counter
print(f"Total time difference between start and end is {finish-start} secs.")