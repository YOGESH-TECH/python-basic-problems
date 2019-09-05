a=int(input("enter the first angle: "))
b=int(input("enter the second angle: "))
c=int(input("enter the third angle: "))
sum=a+b+c
if sum==180:
	print("valid triangle")
elif sum>=180:
	print("not valid as the sum of angles is more than 180")
else:
	print("not valid as the sum of angles is less than 180")
	