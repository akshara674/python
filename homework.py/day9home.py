
class Account:
    def __init__(self, name, balance):
        self._name = name          
        self._balance = balance    

    def __add__(self, other):
    
        return self._balance + other._balance



class SavingsAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.05  



class CurrentAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.02 



if __name__ == "__main__":
    
    savings = SavingsAccount("Ravi", 10000)
    current = CurrentAccount("Anjali", 15000)

    
    print("=== Savings Account Details ===")
    print(f"Account Holder: {savings._name}")
    print(f"Balance: ₹{savings._balance:.2f}")
    print(f"Interest (5%): ₹{savings.calculate_interest():.2f}")
    print()

    
    print("=== Current Account Details ===")
    print(f"Account Holder: {current._name}")
    print(f"Balance: ₹{current._balance:.2f}")
    print(f"Interest (2%): ₹{current.calculate_interest():.2f}")
    print()

    
    total_balance = savings + current
    print("=== Combined Account Summary ===")
    print(f"Total Balance of Ravi and Anjali: ₹{total_balance:.2f}")
