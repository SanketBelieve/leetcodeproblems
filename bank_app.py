#widraw deposit balance
# ac_no = 101
# user=int(input("enter ac no:"))
# action=input("which service u want to use:")
# deposit=0
# widraw=0
# balance=0
# if user==ac_no:
#     if action=='deposit':  
#         deposit=int(input("enter a deposit:"))
#         balance+=deposit
#         print(balance)
#     elif action=='widraw':    
#         widraw=int(input("enter a windraw amount:"))
#         balance-= widraw
#         print("transaction successful")
#         print()
#         if balance==0:
#             print("you don't have any amount in your ac")
#     elif action=='balance':        
#         print(balance)
print("*****Welcome to The Royal Bank*****")
print("**Which service did you want to use, please select option no**")

# def create_account():
#     global balance
#     name=input("Enter Your Name:")
#     phone_no=int(input("enter your phone no:"))
#     addr=input("enter your add:")
#     f_deposit=int(input("enter a ammount:"))
#     balance+=f_deposit

def deposit(deposit_amt):
    global balance
    #deposit_amt = int(input("Enter amount you want to deposit: "))
    balance += deposit_amt
    print("Your current balance is", balance)

def withdraw(withdraw_amt):
    global balance
    #withdraw_amt = int(input("Enter amount: "))
    if withdraw_amt > balance:
        print("Insufficient Balance")
    else:
        balance -= withdraw_amt
        print("Transaction Successful")
        print("You have successfully withdrawn Rs.", withdraw_amt)

def ac_balance():
    print("Your current balance is", balance)

def exit_program():
    print("Thank you for using Our banking Services")

balance = 0

while True:
    print("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
    choice = int(input("Enter a choice: "))

    if choice == 1:
        deposit(int(input("enter deposit amt:")))
    elif choice == 2:
        withdraw(int(input("enter Withdraw Amt:")))
    elif choice == 3:
        ac_balance()
    elif choice == 4:
        exit_program()
        break
    else:
        print("Enter valid Option")
    
                



