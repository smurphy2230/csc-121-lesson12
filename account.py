class Account:

    def __init__(self, name, acct_num, balance):

        """ constructor """

        self.name = name
        self.acct_num = acct_num
        self.balance = balance


    def deposit(self, amt):

        """ deposit money in the account """

        self.balance = self.balance + amt


    def withdraw(self, amt):

        """ withdraw money from account """

        if amt > self.balance:
            print("Withdrawal denied due to insufficient funds.")
        else:
            self.balance = self.balance - amt

