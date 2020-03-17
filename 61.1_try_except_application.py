'''

'''

def func():
    while True:
        try:
            n = int(input("Enter a number: "))
            print(2+n)
        except:
            print("you can enter a number only.")
        else:
            break
    print("Continue further")


func()
