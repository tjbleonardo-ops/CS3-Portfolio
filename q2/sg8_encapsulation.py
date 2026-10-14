#sets attributes
class BankAccount:
    def __init__(self, account_number : int, balance : float):
        self.__account_number = account_number
        self.__balance = balance
      
    @property #prints account number
    def get_account_number(self):
        return f"Account Number: {self.__account_number}"
        
    @property #prints
    def get_balance(self):
        return f"Balance: {self.__balance:.2f}"
    
    def set_account_number(self, account_number):
        self.__account_number = account_number
      
    def set_balance(self, balance):
        print(f"Update balance to {balance:.2f}")
        if balance > 0: 
            self.__balance = balance        
        else:
            print("The balance must not be a negative number.")


a1 = BankAccount(9,10)
account_list = [a1]
for i in range(len(account_list)):
  print(f"Account {i+1}")

print(a1.get_account_number) 
print(a1.get_balance)
print("")
a1.set_account_number(9)
a1.set_balance(-10)

print(a1.get_account_number)
print(a1.get_balance) 
