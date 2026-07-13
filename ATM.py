b= 1022
def balance ():
    print(f"your current balance is:{b}")

def dep():
    global b
    amount=int(input("amount of money you want to deposite:  "))
    if amount>=0 :
        print("Succesful deposite: ")
        print(f"your old balance is {b}")
        b=b+amount
        print(f"your new balance is {b}")
    else:
        print("Invalid deposite amount")


def withdraw():
    global b
    draw=int(input("amount of money you want to withdraw:  "))
    if draw > b or draw<=0 :
        print("Insufficient balance.")
    else: 
        print("Succesful withdraw! ")
        print(f"your old balance is {b}")
        b=b-draw
        print(f"your new balance is {b}")

        


def ATM():
    while True:
        print("1. Check Balance")
        print("2. Make a deposite")
        print("3. withdraw")
        print("4. Exit")
        selected=int(input("please select a number for the needed service  "))
 

        if selected==1:
            balance()
        elif selected==2:
            dep()
        elif selected==3:
            withdraw()
        elif selected==4:
            answer=input("are you sure you want to exit? y/n  ")
            if answer=="y":
                break
        else:
            print("invalid service number ")



print("Welcome to the python ATM!")
ATM()



