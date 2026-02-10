class Bank:
    def __init__(self,balance):
        self.__balance=balance
    def amount(self,amount):
        self.__balance=amount
    def get_amount(self):
        return self.__balance
bank=Bank(2000)
print(bank.get_amount())