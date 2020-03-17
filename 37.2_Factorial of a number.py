
def factorial(n):
    r = 1
    if n < 0:
        return "invalid input"
    else:
       for i in range(1,n+1):
           r = i*r
       return r

result = factorial(-1)
print(result)