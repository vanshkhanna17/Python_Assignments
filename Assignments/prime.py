#prime or not

number=int(input("Enter the number"))
if number==1:
    print("Not prime")
i=2

flag=0
while i<=number:
    if number%i==0:
        flag+=1
    i+=1
   
if(flag==1):
    print("number is prime")
else:
    print("number is not prime")
    
    
#code by sir
n=12
i=2
while i<n:
    if n%i==0:
        print("Not a prime")
        break
else:
    print("Prime")