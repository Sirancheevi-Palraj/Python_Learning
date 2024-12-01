class BankAccount:
    def __init__(self,initalBalance,Number):
        self.initalBalance = initalBalance
        self.Number = Number
    
    def Deposite(self,amount):
        self.initalBalance += amount
        return self.initalBalance

    def withdraw(self,amount):
        self.initalBalance -= amount
        return self.initalBalance
    
    def balance(self):
        return self.initalBalance
     

class customer(BankAccount):
        def __init__(self,initalBalance,Number):
            super().__init__(initalBalance,Number)

        def viewbalnce(self):
           print(self.balance())

# Example Usage
account = BankAccount(1000, 1)
print(account.Deposite(100))  # Output: 1100


customer = customer(2000, 2)  # Create a customer instance
print(customer.viewbalnce())  # Output: Customer balance: 2000

 



       
            