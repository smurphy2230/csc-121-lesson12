#  limiting access to instance variables and methods of an object using
#  getters and setters


class Account:

    def __init__(self, name, acct_num, balance):

        """ constructor - note the __ making them private """

        self.__name = name
        self.__acct_num = acct_num
        self.__balance = balance

    def deposit(self, amt):

        """ deposit money in the account """

        self.__balance = self.__balance + amt

    def withdrawal(self, amt):

        """ withdraw money from account """

        if amt > self.__balance:
            print("Withdrawal amount denied due to insufficient funds.")
        else:
            self.__balance = self.__balance - amt

    # provide access to private instance variables

    def getBalance(self):
        return self.__balance

