balance = 70000000

while True:
    print("""
    Welcome to ATM Machine
    Choose Transaction
    1)BALANCE
    2)WITHDRAW
    3)DEPOSIT
    4)EXIT
    """)
    option = int(input("enter number"))
    if option == 1:
        print("Your balance is ", balance)
    elif option == 2:
        withdraw = float(input("Enter amount to withdraw "))
        if balance > withdraw:
            total = balance - withdraw
            print("success")
            print("your new balance is :", total)
        else:
            print("insufficient Balance")
    elif option == 3:
        deposit = float(input("Enter amount to deposit "))
        total_balance = balance + deposit
        print("success")
        print("total balnace now is: ", total_balance)
    elif option == 4:
        print("Thanks for banking with us")
        exit()
    else:
        print("no selected transaction")
