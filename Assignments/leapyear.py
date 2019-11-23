yr = input('Enter Year: ')
a=int(yr)
if a%400==0:
	print("Leap Year")
elif a%100==0:
	print("Not Leap Year")
elif a%4==0:
	print("Leap Year")
else:
	print("Not Leap Year")