
def play(a = "   ", b = '   ', c ='   ', d = '   ', e = '   ', f= '   ', g = '   ', h = '   ', i ='   '):
    poker = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for s in range(100):
        if (a == b == c == "0") or (a == d == g == "0") or (g == h == i == "0") or (c == f == i == "0") or (
                a == e == i == "0") or (c == e == g == "0"):
            print("0 wins")
            break
        elif (a == b == c == "X") or (a == d == g == "X") or (g == h == i == "X") or (c == f == i == "X") or (
                a == e == i == "X") or (c == e == g == "X"):
            print(" X wins")
            break
        else:
            y = ["first","first", "next","next", "next","next", "next","next", "next","next", "next","next", "next","next", "next","next", "next","next", "next","next", "next","next", "next","next", "next","next", "next","next", "next","next", "next","next", "next","next", "next","next", "next","next", "next","next", "next","next", "next","next", "next","next", "next","next", "next"]

            print(f"     |     |     ")
            print(f" {a} | {b} | {c} ")
            print(f"     |     |     ")
            print(f"-----------------")
            print(f"     |     |     ")
            print(f" {d} | {e} | {f} ")
            print(f"     |     |     ")
            print(f"-----------------")
            print(f"     |     |     ")
            print(f" {g} | {h} | {i} ")
            print(f"     |     |     ")
            print("")

            if s%2==0:
                inp1 = int(input("Player 1 enter your " + y[s] +" position(1-9): " ))
                while inp1 not in poker:
                    print(f"     |     |     ")
                    print(f" {a} | {b} | {c} ")
                    print(f"     |     |     ")
                    print(f"-----------------")
                    print(f"     |     |     ")
                    print(f" {d} | {e} | {f} ")
                    print(f"     |     |     ")
                    print(f"-----------------")
                    print(f"     |     |     ")
                    print(f" {g} | {h} | {i} ")
                    print(f"     |     |     ")
                    print("You cannot choose that")
                    inp1 = int(input("Player 1 enter your " + y[s] + " position(1-9): "))
                if inp1 in poker:
                    poker.remove(inp1)
                pk = None
                if pk == "X" or pk == "x":
                    if inp1 == 1:
                        a = " X "
                    elif inp1 == 2:
                        b = " X "
                    elif inp1 == 3:
                        c = " X "
                    elif inp1 == 4:
                        d = " X "
                    elif inp1 == 5:
                        e = " X "
                    elif inp1 == 6:
                        f = " X "
                    elif inp1 == 7:
                        g = " X "
                    elif inp1 == 8:
                        h = " X "
                    elif inp1 == 9:
                        i = " X "
                else:
                    if inp1 == 1:
                        a = " 0 "
                    elif inp1 == 2:
                        b = " 0 "
                    elif inp1 == 3:
                        c = " 0 "
                    elif inp1 == 4:
                        d = " 0 "
                    elif inp1 == 5:
                        e = " 0 "
                    elif inp1 == 6:
                        f = " 0 "
                    elif inp1 == 7:
                        g = " 0 "
                    elif inp1 == 8:
                        h = " 0 "
                    elif inp1 == 9:
                        i = " 0 "

            else:
                inp2 = int(input("Player 2 enter your " + y[s] + " position: (1-9) "))
                while inp2 not in poker:
                    print(f"     |     |     ")
                    print(f" {a} | {b} | {c} ")
                    print(f"     |     |     ")
                    print(f"-----------------")
                    print(f"     |     |     ")
                    print(f" {d} | {e} | {f} ")
                    print(f"     |     |     ")
                    print(f"-----------------")
                    print(f"     |     |     ")
                    print(f" {g} | {h} | {i} ")
                    print(f"     |     |     ")
                    print("You cannot choose that")
                    inp2 = int(input("Player 2 enter your " + y[s] + " position: (1-9) "))
                if inp2 in poker:
                    poker.remove(inp2)

                    pk = None

                    if pk == "0" or pk == 0:
                        if inp1 == 1:
                            a = " X "
                        elif inp1 == 2:
                            b = " X "
                        elif inp1 == 3:
                            c = " X "
                        elif inp1 == 4:
                            d = " X "
                        elif inp1 == 5:
                            e = " X "
                        elif inp1 == 6:
                            f = " X "
                        elif inp1 == 7:
                            g = " X "
                        elif inp1 == 8:
                            h = " X "
                        elif inp1 == 9:
                            i = " X "
                    else:
                        if inp1 == 1:
                            a = " 0 "
                        elif inp1 == 2:
                            b = " 0 "
                        elif inp1 == 3:
                            c = " 0 "
                        elif inp1 == 4:
                            d = " 0 "
                        elif inp1 == 5:
                            e = " 0 "
                        elif inp1 == 6:
                            f = " 0 "
                        elif inp1 == 7:
                            g = " 0 "
                        elif inp1 == 8:
                            h = " 0 "
                        elif inp1 == 9:
                            i = " 0 "

            print("\n"*100)


play()