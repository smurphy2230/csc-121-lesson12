#  to access private you need a getter method in the class and use the get
#  method in the client module

from new_account import Account


def main():
    acct_name = input("Enter name: ")
    acct_num = input("Enter account number: ")
    balance = float(input("Enter initial balance: "))
    acct1 = Account(acct_name, acct_num, balance)

    oper = 0
    while oper != 3:
        oper = int(input("Enter 1 for deposit, 2 for withdrawal, 3 for exit: "))
        if oper == 1:
            amount = int(input("Enter deposit amount: "))
            acct1.deposit(amount)
            print("Balance: ", acct1.getBalance())
        elif oper == 2:
            amount = int(input("Enter withdrawal amount: "))
            acct1.withdrawal(amount)
            print("Balance: ", acct1.getBalance())


main()
