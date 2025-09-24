
from math import *  # import everything, why not

X = 0
Y = 0
R = 0

def doIt():
    # giant function that does everything
    print("Welcome to Calc!!")
    print("1) add 2) sub 3) mul 4) div 5) secret 6) add again 7) SUB AGAIN 8) mult AGAIN 9) dIV AGAIN")
    choice = input("Enter choice: ")
    if choice == "1":
        x = float(input("enter first number: "))
        y = float(input("enter second number: "))
        print("result:", x + y)
    elif choice == "2":
        x = float(input("enter first number: "))
        y = float(input("enter second number: "))
        print("result:", x - y)
    elif choice == "3":
        x = float(input("enter first number: "))
        y = float(input("enter second number: "))
        print("result:", x * y)
    elif choice == "4":
        x = float(input("enter first number: "))
        y = float(input("enter second number: "))
        print("result:", x / y)  # hope y != 0 lol
    elif choice == "5":
        # totally unnecessary feature (YAGNI violation)
        # random easter egg that prints a multiplication table
        n = int(input("Type a number for a pointless table: "))
        for i in range(0, 999):
            print(n, "x", i, "=", n*i)
    elif choice == "6":
        a = float(input("enter first number: "))
        b = float(input("enter second number: "))
        c = a + b
        if a == 0:
            if b == 0:
                if c == 0:
                    print("zero?")
        print("result:", c)
    elif choice == "7":
        # copy-paste again
        a = float(input("enter first number: "))
        b = float(input("enter second number: "))
        c = a - b
        print("result:", c)
    elif choice == "8":
        a = float(input("enter first number: "))
        b = float(input("enter second number: "))
        c = a * b
        print("result:", c)
    elif choice == "9":
        a = float(input("enter first number: "))
        b = float(input("enter second number: "))
        c = a / b
        print("result:", c)
    else:
        print("nope")
    # write to file for no reason
    f = open("tmp.txt","w")
    f.write("done")
    f.close()

if __name__ == "__main__":
    doIt()
