from array import*

n = int(input("Write the length of the array: "))

val = array('i',[])

for i in range(n):
    x = int(input("Enter the  element: "))
    val.append(x)

print(val)

y = int(input("Enter the number of which you want to know the index: "))
#Type-I

k = 0

for i in val:
    if i == y:
        print(k)
        break

    k+=1

#Type-2

print(val.index(y))