class BankAccount:
    def __init__(self, account_number : int, balance : float):
        self.__account_number = account_number
        self.__balance = balance

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def set_balance(self, balance):
        if not balance < 0: 
            self.__balance = balance,           
        else:
            print("hi")
    @property
    def get_account_number(self):
        return f"Account Number {self.__account_number}"
        
    @property
    def get_balance(self):
        return f"Balance {self.__balance}"

a1 = BankAccount(111,-100.0)
