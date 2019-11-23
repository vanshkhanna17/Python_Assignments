a=int(input("Enter number of lines: "))
st="python"
for n in range(1,a+1):
    print()
    print(n*"* ")

for n in range(a,0,-1):
    print()
    print(n*"* ")
    
for n in range(a,0,-1):
    print()
    print((a-n)*" "+n*"*")
    
for n in range(0,a+1):
    print()
    print((a-n)*" "+n*"*")
    
for n in range(0,a+1):
    print()
    print((a-n)*" "+n*"* ")
    
for n in range(a,0,-1):
    print()
    print((a-n)*" "+n*"* ")
    
for n in range(0,len(st)):
    print()
    print((len(st)-n)*" "+st[:n+1],end=" ")
print()
print()
st1=''
b=0
c=1
print(str(b)+", "+str(c)+",",end=" ")
for n in range(1,a-1):
    sum = b+c
    b=c
    c=sum
    st1 = st1+str(sum)+", "
print(st1)