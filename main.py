# Pyhton Banking Program

def showBalance():
    print(f"Your Balance is: ${balance:.2f}")

def deposit():
    amnt = float(input("Enter the amount to be deposited: $"))
    if amnt<0:
        print("Enter the valid amount")
        return 0
    else:    
        return amnt
    
def withdraw():
    amnt = float(input("Enter the amount to be withdrawn: $"))
    if amnt > balance:
        print("Insufficient Balance")
        return 0
    elif amnt < 0:
        print("Enter the valid amount")
        return 0
    else:
        return amnt    
    

balance = 0
is_Running = True

while is_Running:
    print("Ok Bank")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    
    choice = input("Enter the selected choice(1-4): ")
    
    if choice == "1":
        showBalance()
    
    elif choice == "2":
        balance += deposit()
    
    elif choice == "3":
        balance += withdraw()

    elif choice == "4":
        is_Running = False
    
    else:
        print("Enter valid choice.")
    
print("GoodBye")     