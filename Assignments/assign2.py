#assignment for marks (multiple condition)

marks= int(input('Enter marks'))
if marks>=0 and marks<= 100:
    print("valid")
    if marks>=0 and marks<= 39:
        print("Fail")
    elif marks>=40 and marks<=59:
        print("Third")
    elif marks>=60 and marks<=79:
        print("Second")
    elif marks>=80 and marks<=100:
        print("First")
else:
    print("invalid")