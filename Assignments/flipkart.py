class product:
    def __init__(o, name, cost, brand, rating, discount, category):
        o.name = name
        o.cost = cost
        o.brand = brand
        o.rating = rating
        o.discount = discount
        o.category = category

    def pri(o):
        return o.name, o.cost, o.brand, o.rating, o.discount, o.category


ls = [
    product("AC", 27000, "LG", 4, 20, "Electronics"),
    product("Fridge", 4000, "LG", 5, 20, "Electronics"),
    product("WashingMachine", 5000, "Samsung", 4, 15, "Electronics"),
    product("HP202", 5000, "HP", 4, 15, "Laptops"),
    product("le202", 20000, "Lenovo", 4, 15, "Laptops")
     ]

ls.sort(key=lambda el: el.name)
for i in ls:
    print(i.pri(), end=", ")
print()
ls.sort(key=lambda el: int(el.cost))
for i in ls:
    print(i.pri(), end=", ")
print()
ls.sort(key=lambda el: int(el.cost), reverse=True)
for i in ls:
    print(i.pri(), end=", ")
print()
ls.sort(key=lambda el: int(el.rating))
for i in ls:
    print(i.pri(), end=", ")
print()
ls.sort(key=lambda el: int(el.discount))
for i in ls:
    print(i.pri(), end=", ")
print()
ls.sort(key=lambda el: int(el.discount), reverse=True)
for i in ls:
    print(i.pri(), end=", ")
print()

newobj= filter(lambda el: el.brand == "LG", ls)
print(type(newobj))
for i in newobj:
    print(i)

newobj = filter(lambda el: el.category == "Laptops", ls)
print(type(newobj))
for i in newobj:
    print(i)


choice = input("Enter the choice ")
print(ls.sort(key=lambda el: int((el[choice])), reverse=True))