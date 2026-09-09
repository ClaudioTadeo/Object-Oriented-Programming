
class laptop:
    def _init_(self, color, material, size):
        self.color = color
        self.material = material
        self.size = size

        def move(self):
            print("The laptops is on")

        def describe(self):
            print(f"The laptop is made with {self.material}")

# Create multiple instances using the class "Laptop"
laptop1 = laptop("black", "metal", "16p")
laptop2 = laptop("white", "steel", "12p")

print(laptop1.material)
print(laptop2.material)
laptop1.describe()
laptop2.describe()

class BankAccount:
    def __init__(self, holder_name, initial_balance):
        self.holder = holder_name
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"-> Depósito exitoso de ${amount}.")
        else:
            print("-> Error: El monto a depositar debe ser mayor a cero.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("-> Error: Fondos insuficientes.")
        elif amount <= 0:
            print("-> Error: El monto a retirar debe ser mayor a cero.")
        else:
            self.__balance -= amount
            print(f"-> Retiro exitoso de ${amount}.")

    def check_balance(self):
        print(f"Saldo actual: ${self.__balance}")


account1 = BankAccount("Raúl Pérez", 5000)
account2 = BankAccount("Joel López", 3000)

print(f"Titular: {account1.holder}")
account1.check_balance()
account1.deposit(500)
account1.withdraw(200)
account1.check_balance()

print("-" * 40)

print(f"Titular: {account2.holder}")
account2.check_balance()
account2.deposit(1000)
account2.withdraw(500)
account2.check_balance()

