import random
import string

print("Password Generator & Strength Checker!\n")

def inp():
    choice = input("Enter Choice: ")
    if(choice.isdigit()):
        choice=int(choice)
        if(1<=choice<=6):
            return choice
        else:
            print("Invalid Input, Number must be from 1 to 3.\n")
            return inp()
    else:
        print("Invalid Input, Please choose a number.\n")
        return inp()

def uppercase():
    upper = input("Include uppercase letters ? (y/n): ").strip().lower()
    if upper != "y" and upper != "n":
        print("Invalid Input. Enter 'y' for yes or 'n' for no.\n")
        return uppercase()
    return upper

def numbers():
    number = input("Include numbers ? (y/n): ").strip().lower()
    if number != "y" and number != "n":
        print("Invalid Input. Enter 'y' for yes or 'n' for no.\n")
        return numbers()
    return number

def symbols():
    symbol = input("Include symbols ? (y/n): ").strip().lower()
    if symbol != "y" and symbol != "n":
        print("Invalid Input. Enter 'y' for yes or 'n' for no.\n")
        return symbols()
    return symbol

def gen():
    password=""
    length = input("Enter length of password: ")
    if(length.isdigit()):
        length=int(length)
        if(0<length<=50):
            upper = uppercase()
            number = numbers()
            symbol = symbols()

            possiblelist=list(string.ascii_lowercase)
            if upper == "y":
                possiblelist+=list(string.ascii_uppercase)
            if number == "y":
                possiblelist+=list("0123456789")
            if symbol == "y":
                possiblelist+=list(string.punctuation)
            password = "".join(random.choice(possiblelist) for _ in range(length))
            return password

        else:
            print("Password Length must be atleast 1 and max 50 characters.\n")
            return gen()
    else:
        print("Invalid Input! Please enter a Valid length.\n")
        return gen()

def check():
    lowletters=0
    upletters=0
    nums=0
    syms=0
    password=input("Enter password: ").strip()
    if not password:
        print("Cant enter an empty password.\n")
        return check()
    for i in password:
        if i in list(string.ascii_lowercase):
            lowletters+=1
        elif i in list(string.ascii_uppercase):
            upletters+=1
        elif i in list(string.punctuation):
            syms+=1
        elif(i==" "):
            pass
        else:
            nums+=1
    print(f"\nYour password contains:\n{lowletters} Lowercase letters")
    print(f"{upletters} Uppercase letters")
    print(f"{nums} Numbers")
    print(f"{syms} Symbols\n")

    if(len(password)<6):
        print("Password Strength: Weak (Short Length)\n")
    elif(nums==0 and syms==0):
        print("Password Strength: Weak (Only Letters)\n")
    elif(syms==0 and (lowletters==0 and nums !=0))or(syms==0 and (upletters==0 and nums !=0)or(syms==0 and nums!=0)):
        print("Password Strength: Medium (No Symbols)\n")
    elif(nums==0 and (lowletters!=0 and syms!=0))or(nums==0 and (upletters!=0 and syms!=0))or(nums==0 and syms!=0):
        print("Password Strength: Medium (No Numbers)\n")
    elif(lowletters !=0 or upletters !=0) and (nums !=0 and syms !=0):
        print("Password Strength: Strong (Includes letters, numbers and special characters)\n")

def leave():
    print("Thank You!")
    exit()

while True:
    print("1. Generate a Password")
    print("2. Check Strength of Password")
    print("3. Exit\n")
    choice = inp()
    if choice == 1:
        password=gen()
        print(f"\nGenerated Password: {password}\n")
    elif choice == 2:
        check()
    else:
        leave()