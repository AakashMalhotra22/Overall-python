n = int(input("Tell the length of the list: "))
lst = []

for i in range(n):
    x = int(input("Enter the first element: "))
    lst.append(x)

def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2 == 0:
            even+=1
        else:
            odd+=1
    print("even = ", even)
    print("odd = ", odd)

count(lst)


# modified

print(" ")
def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2 == 0:
            even+=1
        else:
            odd+=1
    return even, odd


even1, odd1 = count(lst)

print("Even : {} and Odd : {}".format(even1, odd1) )