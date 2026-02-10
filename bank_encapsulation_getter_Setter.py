class Bank:
    def __init__(self,balance):
        self.__balance=balance
    def set_balance(self,amount):
        self.__balance=amount
    def get_balance(self):
        return self.__balance
bank=Bank(2000)
print(bank.get_balance())
bank.set_balance(5000)
print(bank.get_balance())