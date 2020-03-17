'''
filter:
1. syntax:
   filter(function_name, iterator)

2. It filters out the value from the iterator, what it does it iterate through the iterator and check either the value in the iterator satisfies the condition of the function
   and if it does then it would pass that value to filter object from where you can print it out the value otherwise if it doesnot satisfy the condition it skips it.
   Example:
       for example we have even number function and a iterator consists of value from 0 to 10 then, it would iterate through each value of iterator and checks whether the iterated
       value is even or not if it is even then it would be passed to filter object from where you can print it out otherwise that value will be skipped.

3. In this output is obtained from the iterator.
'''
'''
Basic examples
'''

nums = [3,2,6,8,4,6,2,9]

# Way-1
def is_even(n):
    return n%2==0

evens = list(filter(is_even, nums))

print(evens)

print(" ")

# Way-2

is_evens = lambda n: n%2 == 0

evens = list(filter(is_even, nums))

print(evens)

print("")

# Way -3
evens = list(filter(lambda n: n%2 ==0, nums))
print(evens)

print("")
# Way- 4

evens = (filter(lambda n: n%2 ==0, nums))
for i in evens:
    print(i)


#Type-2

str = ["", "aakash", "ram", "shyam", ""]
remove_empty_str = list(filter(None, str))
print(remove_empty_str)

#False values = "", 0.0, 0j, [],(),{},False, None, instances signal they are empty.