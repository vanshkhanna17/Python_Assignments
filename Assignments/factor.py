#factors of a number

number=int(input("Enter the number"))
i=1
while i<=number:
    if number%i==0:
        print(i)
    i+=1

#count factors
number1=int(input("Enter the number"))
i=1
c=0
while i<=number1:
    if number1%i==0:
        #print(i)
        c+=1
    i+=1
print(c)


#sum factors
number2=int(input("Enter the number"))
i=1
s=0
while i<=number2:
    if number2%i==0:
        #print(i)
        s+=i
    i+=1
print(s)