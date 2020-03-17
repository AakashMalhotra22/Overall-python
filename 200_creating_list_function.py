n = int(input("Tell me the number of person do you want to  use: "))
lst = []
for i in range(n):
    x = input("Tell the " + str(i+1)+ "st name: ")
    lst.append(x)

print(lst)

def count(lst1):
    llt5 = 0
    lgte5 = 0
    for i in lst1:
        if len(i)<5:
            llt5+=1
        else:
            lgte5+=1
    return llt5, lgte5

llt5, lgte5 = count(lst)

print("Big : {} and Small : {}".format(llt5, lgte5))