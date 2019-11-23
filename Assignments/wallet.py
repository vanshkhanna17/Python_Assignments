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

    def show():
        print("Available Balance: ", balance)

    def transfer(wal, amount):
        nonlocal balance
        if amount <= balance:
            balance = balance - amount
            dic = wal
            dic["deposit"](amount)
            print(amount, " deducted from wallet. New Balance: ", balance)

    d = {"deposit": deposit, "spent": spent, "show": show, "transfer": transfer }
    # li = [deposit, spent, show]
    return d


d1 = wallet(1000)
d2 = wallet(500)
# deposit = l1[0]
# spent = l1[1]
# show = l1[2]
d1["transfer"](wallet(40), 500)
d1["show"]()
d1["deposit"](400)
d1["spent"](900)
d1["show"]()

# swapping
a, b = 10, 20
b, a = a, b
print(a, b)

# template
data = "I am a {0} from {1}"
sub1 = 'string'
lang = 'Python'
print(data.format(sub1, lang))

temp='''Hello {fname} {lname}, 
Welcome to {city}'''
print(temp.format(fname="Sachin", lname='Tendulkar', city="Bhind"))

ob={
    'fname': "Rahul",
    'lname': "Dravid",
    'city': "Bhinda"
}
temp='''Hello {fname} {lname}, 
Welcome to {city}'''
print(temp.format(**ob))


li = [{
'fname': "sachin",
    'lname': "tendulkar",
    'city': "Bhind"
},
    {'fname': "Rahul",
    'lname': "Dravid",
    'city': "Bhinda"
},
    {
'fname': "sourav",
    'lname': "ganguly",
    'city': "Bhinde"
}]
print()
for i in li:
    temp = '''Hello {fname} {lname}, 
    Welcome to {city}'''
    print(temp.format(**i))