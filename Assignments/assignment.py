def wallet(balance):
    def deposit(amount):
        nonlocal balance
        balance = balance + amount
        print(amount, " added to wallet. New Balance: ", balance)

    def spent(amount):
        nonlocal balance
        if amount <= balance:
            balance = balance - amount
            print(amount, " deducted from wallet. New Balance: ", balance)
        else:
            print("Insufficient Balance")

    def transfer(wal, amount):
        nonlocal balance
        if amount <= balance:
            balance = balance - amount
            dic = wal
            dic["deposit"](amount)
            print(amount, " deducted from wallet. New Balance: ", balance)

    def show():
        print("Available Balance: ", balance)
    #li = [deposit, spent, show]  #list of functions
    li = {"deposit": deposit, "spent": spent, "show": show}    #dict of functions
    return li

l1=wallet(1000)
l1["show"]()
l1["deposit"](400)
l1["spent"](200)
l1["show"]()


#deposit = l1[0]
#spent = l1[1]
#show = l1[2]
#show()
#deposit(500)
#spent(1200)
#show()