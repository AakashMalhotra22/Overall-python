'''
Comparing time difference between normal function and generator function, executing the same thing.
'''
import memory_profiler
import time

#Normal function using return keyword
def check_even(numbers):
    even = []
    for num in numbers:
        if num%2 ==0:
           even.append(num)
    return even

if __name__ == "__main__":
    m1 = memory_profiler.memory_usage()
    t1 = time.perf_counter()
    c1= check_even(range(10000000))

    t2 = time.perf_counter()
    m2 = memory_profiler.memory_usage()
    time_diff = t2-t1
    mem_diff = m2[0]-m1[0]
    print(f"Python program took {time_diff} Secs and {mem_diff} Mb to execute normal function using return keyword.")

# Generator function using yield.

def check_even(numbers):
    even = []
    for num in numbers:
        if num % 2 == 0:
            yield num


if __name__ == "__main__":
    m1 = memory_profiler.memory_usage()
    t1 = time.perf_counter()
    c1 = check_even(range(10000000))

    t2 = time.perf_counter()
    m2 = memory_profiler.memory_usage()
    time_diff = t2 - t1
    mem_diff1 = m2[0] - m1[0]+mem_diff #here mem_diff is added because m1[0] also contains the memory of normal function execution.
    print(f"Python program took {time_diff} Secs and {mem_diff1} Mb to execute generator function using yield keyword.")
