#assignment 
balance = int(input("Enter the Balance"))
def wallet(balance):
  
    def deposit(amount):
        global balance
        amount = int(input("Enter the amount to withdraw"))
        balance+= amount
        print("deposited amount:" + amount)
        print("new balance:" +balance)
    return deposit
    def withdraw(amount):
        global balance
        amount = int(input("Enter the amount to withdraw"))
        if(amount<balance):
            return balance -= amount
        else:
            return ("insufficient balance")
        print("amount" +amount)
        print("new balance"+ balance)
    return withdraw
print(balance)