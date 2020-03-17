def sort(l):
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]





list = [6,5,114,3,2,1]

sort(list)

print(list)