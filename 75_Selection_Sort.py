'''
Selection sort:
1. In this we first iterate through the list from index position 0 to end, to find the minimum value and keep that value
   at the index zero of the list, then again, iterate through the loop from index position 1 to end and find the minimum
   value and keep that minimum value at the index position 1, then again iterate through the loop from index position 2 to
   end and find the minimum value of the list and keep that value at index position 2 and this process goes on, till the
   whole list is exhausted.
   By this way, we can sort a list.
   This is called selection sort.

2. It uses less memory as compared to bubble sort.

3. We can also do selection sort by considering the max value.



'''

def sort(l):
    for i in range(len(l)-1):
        minvalue = i
        for j in range(i, len(l)):
            if l[j]<l[minvalue]:
                minvalue = j

        temp = l[i]
        l[i] = l[minvalue]
        l[minvalue]= temp




list = [6,5,114,3,2,1]

sort(list)

print(list)

L1 =[0,1,1]
L2 = [1,0,1]

