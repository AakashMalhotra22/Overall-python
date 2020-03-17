import sys
m = int(input("Tell the number: "))
sys.setrecursionlimit(m+100001)

a = 0
def fac(n):
    if n == 0:
        return 1
    return n* fac(n-1)

result = fac(m)
print(result)