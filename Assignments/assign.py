#assignment

data="Hello World"
def demo():
    global data #global keyword to rewrite the data value to hello universe
    #same is for non local
    data="Hello Universe"
    print(data)
demo()
print(data)


count=0
def hello():
    global count
    count+=1
    print(count)

def bye():
    global count
    count=100
hello()
hello()
bye()
hello()
hello()


def container():
    count= 0
    def inner(): #fuction is also a data type
        nonlocal count
        count+=1
        print(count)
    return inner
hello=container() #referenced is passed to the hello
hello() #bcoz of lexical reference/link--- it can acess the count
#clouser --creating function but can access the inner function outside the function
hello()
hello()
hi=container() #both hi and hello count is different this is clouser
hi()
hi()
hi()
hi()
hello()