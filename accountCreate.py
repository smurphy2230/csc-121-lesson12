from account import Account


def main():
    acct_name = input("Enter name: ")
    acct_num = input("Enter account number: ")
    balance = float(input("Enter initial balance: "))
    acct1 = Account(acct_name, acct_num, balance)
    print("Balance: ", acct1.balance)
    oper = 0
    while oper != 3:
        oper = int(input("Enter 1 for deposit, 2 for withdrawal,"
                         "3 for exit: "))
        if oper == 1:
            amount = float(input("Enter deposit amount: "))
            acct1.deposit(amount)
            print("Balance: ", acct1.balance)
        elif oper == 2:
            amount = float(input("Enter withdrawal amount: "))
            acct1.withdraw(amount)
            print("Balance: ", acct1.balance)


main()
