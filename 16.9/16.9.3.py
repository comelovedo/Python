# Need to write a program that processes data,
# and get the following at the console output: Client "...". Balance: "..." rub.

class E_Wallet:
    def __init__(self, name="", balance=0):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Customer: {self.name}, Balance: {self.balance} rub."


a = str(input("Input your name: "))
b = int(input("Available amount: "))

Customer_1 = E_Wallet(a, b)
print(Customer_1)
