from src.account import BankAccount

# child class      
class SavingsAccount(BankAccount): 
    MIN_BALANCE = 500  # Class Attribute

    def apply_interest(self,interest = 0.05):
        if self.balance >= SavingsAccount.MIN_BALANCE:
            print("Interest Applied!")
            self.balance += self.balance * interest
        else:
            print(f"Minimum balance {SavingsAccount.MIN_BALANCE} not met — no interest")
        return self