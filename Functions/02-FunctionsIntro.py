print("""
1. ATM
2. Net Banking
3. Bank Transaction
""")

user_choice = input("Enter your choice : ")

# function defination
def withdraw():
    total_bal = 10000
    amount = int(input("Enter the amount you want to withdraw : "))
    if amount > total_bal:
        print("Insufficient Balance")
    else:
        total_bal = total_bal - amount
        print("Withdraw successfull...")
        print("Remaining balance is", total_bal)

if user_choice == "1":
    pin = input("Enter your PIN : ")
    if pin == "1234":
        print("Welcome")
        withdraw() # function call
    else:
        print("Invalid PIN")

elif user_choice == "2":
    user_id = input("Enter your ID : ")
    password = input("Enter your password : ")

    if user_id == password:
        print("Login Success")
        withdraw()
    else:
        print("Id Password do not match")

elif user_choice == "3":
    account_no = input("Enter your account number : ")
    if account_no == "1234567890":
        print("Login Success")
        withdraw()
    else:
        print("Wrong Account Number")