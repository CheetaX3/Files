# инкапсуляция
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Вы ввели отрицательную сумму")
        self._balance = value
    
    def deposit(self, amount): 
        if amount < 0:
            raise ValueError("Сумма должна быть положительной")
        self._balance += amount
    
    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Недостаточно средств на счёте")
        self._balance -= amount

    def calculate_interest(self, period, rate):
        return (self._balance * rate * period) / 100

account_1 = BankAccount("123456789", 1000)
print(account_1.balance)
account_1.deposit(500)
account_1.withdraw(200)
print(account_1.balance)
account_1.balance = -100
