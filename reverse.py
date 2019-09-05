num1=int(input("enter the no. here: "))
orig=num1
reverse=0
while num1>0:
	new=num1%10
	reverse=(reverse*10)+new
	num1=num1//10
print("reverse of the no. is:",reverse)

if orig==reverse:
	print("reverse is equal to original")
else:
	print("reverse is not equal to orignal")