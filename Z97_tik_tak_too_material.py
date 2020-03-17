from random import*
from time import sleep
def tik_tak_too_game():
    c1 = True
    while c1:
        print("Welcome to tik_tak_too_game.".upper())
        input1 = input("Choose between X and 0(Zero): ")
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

        sleep(10)
        print("Let's begin: ")
        y4 =[3,2,1, "Go"]
        for i in y4:
            print(i)
            sleep(1)




















        input100 =input("Do you want to play again Yes or No: ")
        if input100 in ["Yes", "yes", "ya"]:
            c1 = True
        else:
            c1 = False
    else:
        print("ok, thanks for playing this game.")


tik_tak_too_game()

