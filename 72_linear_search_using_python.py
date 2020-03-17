x = int(input("Enter what are you looking for?? "))

arr = [5,8,4,9,2]
k = 1
for i in arr:


    if i == x:
        print(str(i) + " is in the list and it's position is " +str(k) + " in the list.")
        break
    k += 1


else:
   print(str(x) +" does not in the list.")


print("               ")
# 2nd way by make a  function.

n = int(input("Enter any number: "))
x = ""
def search(n, list):
   for i in range(len(list)):
        if list[i] == n:
             globals()['x']=i
             return True

list = [1,2,3,4,5,6]

if search(n, list):
    print("found at ", x+1)

else:
    print("Not found")

