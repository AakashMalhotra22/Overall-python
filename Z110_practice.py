a = ""
b = ""
c = ""
d = ""
e = ""
f = ""
g = ""
h = ""
i = ""
y = input("choose either X or 0:" )
if y == 'x' or y == 'X':
    z1 = 'player 1'
    z2 = 'player 2'
else:
    z1 = 'player 2'
    z2 = 'player 1'
for i in range(100):
    if (a == b == c=="0") or (a == d == g =="0") or (g == h == i=="0") or (c==f==i=="0") or (a==e==i=="0") or (c==e==g=="0"):
        print(z2+"wins")
        break
    elif(a == b == c=="X") or (a == d == g =="X") or (g == h == i=="X") or (c==f==i=="X") or (a==e==i=="X") or (c==e==g=="X"):
        print(z1+"wins")
        break
    else:
        in1 = int(input("Enter the position player 1: "))
        in2 = None

        input1 = None
        inp1 = None
        inp2 = None

        print(f"     |     |     ")
        print(f" {a} | {b} | {c} ")
        print(f"     |     |     ")
        print(f"-----------------")
        print(f"     |     |     ")
        print(f" {d} | {e} | {f} ")
        print(f"     |     |     ")
        print(f"-----------------")
        print(f"     |      |     ")
        print(f" {g} |  {h} | {i} ")
        print(f"     |      |     ")

        in2 = int(input("Enter the position player 2: "))
