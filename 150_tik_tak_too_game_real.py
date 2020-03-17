from random import*
from time import sleep
def tik_tak_too_game():
    c1 = True
    while c1:
        print("Welcome to tik_tak_too_game.".upper())
        input1 = input("Choose between X and 0(Zero): ");
        y = ['x',"X", 0, "0"]

        while input1 not in y:
            input1 = input("you cannot choose this, choose between X and 0(Zero): ")
        y1 = ['x', "X"]
        if input1 in y1:
            p2 = "0"
        else:
            p2 = "X"

        z1 = choice([["x", "x"], [0,"0"]])
        if input1 in z1:
            print("")
            print( (input1) +" is Player 1 and will move first.")
            print(p2+" is Player 2 and will move after player 1.")
            pk = input1
        else:
            print("")

            print(p2 + " is player 1 and will move first.")
            print((input1) + " is player 2 and will move after player 1.")
            pk = p2

        print("   ")

        input("Press any key to continue: " )
        if input:
          print("Let's begin: ")
          y4 =[3,2,1, "Go"]
          for i in y4:
              print(i)
              sleep(1)
          print("\n"*100)

          def play(a="   ", b='   ', c='   ', d='   ', e='   ', f='   ', g='   ', h='   ', i='   '):
              poker = [1, 2, 3, 4, 5, 6, 7, 8, 9]
              for s in range(100):
                  if (a == b == c == " 0 ") or (a == d == g == " 0 ") or (g == h == i == " 0 ") or (
                          c == f == i == " 0 ") or (
                          a == e == i == " 0 ") or (c == e == g == " 0 ") or (d == e ==f == " 0 ") or(b==e==h==" 0 "):
                      print("")
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
                      print("0 WINS")
                      break
                  elif (a == b == c == " X ") or (a == d == g == " X ") or (g == h == i == " X ") or (
                          c == f == i == " X ") or (
                          a == e == i == " X ") or (c == e == g == " X ") or (d == e ==f == " X ")or(b==e==h==" X "):
                      print("")
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
                      print("X WINS")
                      break
                  elif a in[" x ", " X ", 0 , " 0 "] and b in[" x ", " X ", 0 , " 0 "] and c in[" x ", " X ", 0 , " 0 "] and d in[" x ", " X ", 0 , " 0 "] and e in[" x ", " X ", 0 , " 0 "] and f in [" x ", " X ", 0, " 0 "] and g in[" x ", " X ", 0 , " 0 "] and h in[" x ", " X ", 0 , " 0 "] and i in[" x ", " X ", 0 , " 0 "]:
                      print("")
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

                      print("Match draw".upper())
                      break
                  else:
                      y = ["first", "first", "next", "next", "next", "next", "next", "next", "next", "next", "next",
                           "next", "next", "next", "next", "next", "next", "next", "next", "next", "next", "next",
                           "next",
                           "next", "next", "next", "next", "next", "next", "next", "next", "next", "next", "next",
                           "next",
                           "next", "next", "next", "next", "next", "next", "next", "next", "next", "next", "next",
                           "next",
                           "next", "next"]
                      print("")

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

                      if s % 2 == 0:
                          inp1 = None
                          while inp1 not in range(1,10):
                            try:
                                inp1 = int(input("Player 1 enter your " + y[s] + " position(1-9): "))
                            except:
                                 print("Please enter the correct position.")

                          while inp1 not in poker:
                              print("")
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
                          inp2 = None
                          while inp2 not in range(1,10):
                            try:
                                inp2 = int(input("Player 2 enter your " + y[s] + " position: (1-9) "))
                            except:
                                 print("Please enter the correct position.")

                          while inp2 not in poker:

                              print("")
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

                              if pk == "0" or pk == 0:
                                  if inp2 == 1:
                                      a = " X "
                                  elif inp2 == 2:
                                      b = " X "
                                  elif inp2 == 3:
                                      c = " X "
                                  elif inp2 == 4:
                                      d = " X "
                                  elif inp2 == 5:
                                      e = " X "
                                  elif inp2 == 6:
                                      f = " X "
                                  elif inp2 == 7:
                                      g = " X "
                                  elif inp2 == 8:
                                      h = " X "
                                  elif inp2 == 9:
                                      i = " X "
                              else:
                                  if inp2 == 1:
                                      a = " 0 "
                                  elif inp2 == 2:
                                      b = " 0 "
                                  elif inp2 == 3:
                                      c = " 0 "
                                  elif inp2 == 4:
                                      d = " 0 "
                                  elif inp2 == 5:
                                      e = " 0 "
                                  elif inp2 == 6:
                                      f = " 0 "
                                  elif inp2 == 7:
                                      g = " 0 "
                                  elif inp2 == 8:
                                      h = " 0 "
                                  elif inp2 == 9:
                                      i = " 0 "

                      print("\n" * 100)

          play()

          input100 =input("Do you want to play again Yes or No: ")
          if input100 in ["Yes", "yes", "ya", "YES"]:
            c1 = True
          else:
            c1 = False
    else:
        print("ok, thanks for playing this game.")


tik_tak_too_game()

