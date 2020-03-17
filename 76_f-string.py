# Normal
r = "sita"
r1 = 3
y = f"ram is {r} and {r1}"
y = f"ram is {r.upper()} and {r1}"# You can also you functions in f string
print(y)

#2. dictinory

d = {"name": "ram", "age": 23}

y = f"My name is {d['name']} and my age is {d['age']}."# diclaimer: string should have different quotes the quotes which are inside
print(y)


# 3. Calculation
y = f"4 times 11 is equals to {4*11}"

print(y)


#4. for loop
for n in range(1,11):
    y = f"The value is {n:02}"
    print(y)

# floating point values

pi = 3.14159

y = f"Pi is equals to {pi:.3f}"
print(y)


# datetime
from datetime import datetime

birthday = datetime(2000,7,22)

print(f"Jehn has a birthday on {birthday}")
# some formatting
print(f"aakash has a birthday on {birthday: %B, %d,%Y}")