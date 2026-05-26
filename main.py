from src.account import BankAccount
from src.savings import SavingsAccount

if __name__ == "__main__": 
    print("--- BankAccount ---")
    b1 = BankAccount(1,100)
    b2 = BankAccount(1,200)
    print(b1==b2)

    print("\n--- SavingsAccount ---")
    s1= SavingsAccount(1,430)
    s1.deposit(70) 
    s1.apply_interest()
    s1.withdraw(1000) #method calling
    print(f"Final balance: {s1.balance}")