#Class inheritance
class BankAccount:
    def __init__(self,balance=0):
        self.balance = balance
    def withdraw(self,amount=0):
        self.balance -= amount
        print(f"Withdrew {amount} — Balance: {self.balance}")
        return self
class SavingsAccount(BankAccount):
    
    def apply_interest(self,interest_rate = 0.05):
        self.balance *= (1+interest_rate)
        print(f"Interest applied — Balance: {self.balance}")
        return self


if __name__ == "__main__":
    s1 = SavingsAccount(1000)
    print(s1.balance) 
    s1.withdraw(200)         
    s1.apply_interest(0.08)    
    print(s1.balance)  


class Employee:
    MIN_SALARY = 30000 # Class attribute 
    def __init__(self,name,salary): # self is to be defined object
        self.name = name # ATTRIBUTE
        if salary >= Employee.MIN_SALARY:
            self.salary = salary # INSTANCE ATTRIBUTE
        else:
            self.salary = Employee.MIN_SALARY
            print("Invalid Salary")
        print('__init__ called')
    def identify(self): # METHOD (function inside class)
        print("My name is",self.name.title())
        return self
    def show_salary(self): # METHOD (function inside class)
        print(f"{self.name}'s Salary:", self.salary)
        return self
    def set_bonus(self,bonus=0): # METHOD (function inside class)
        self.salary += bonus # ATTRIBUTE
        return self

# This runs when you execute the file
if __name__ == "__main__":
    emp1 = Employee('Sangita',80000) #Object
    emp1.show_salary()
    emp1.set_bonus(400).show_salary()
    emp2 = Employee("Arijit", 20000)   # triggers invalid salary
    emp2.show_salary()
