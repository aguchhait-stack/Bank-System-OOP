class BankAccount:
    def __init__(self,account_id,balance):

        self.account_id = account_id #Attribute
        self.balance = balance #Attribute

    def __eq__(self,other):
        print("__eq__ is called")
        return (self.account_id == other.account_id) and\
            (type(self)==type(other))

    def deposit (self,deposit): #Method
        self.balance += deposit
        return self
    
    def withdraw (self,debit): #Method
        if debit > self.balance:
            print('Not Enough balance to withdraw!')
            return self
        else:
            self.balance -= debit
            return self