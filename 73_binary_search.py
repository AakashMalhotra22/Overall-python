'''
In binary search, the list should be sorted.
'''

n = int(input("Enter any number: "))
x = ""
def search(n, list1):
   l =0
   u = len(list1) -1
   while l<= u:
           mid = (l+u)//2

           if list1[mid] == n:
               globals()['x'] = mid

               return True
           else:
               if mid<n:
                   l = mid+1


               else:
                   u = mid-1

list1 = list(range(100))

if search(n, list1):
    print("found at ", x+1)

else:
    print("Not found")
