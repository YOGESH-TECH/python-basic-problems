for i in range(1,11):
	n=int(input("enter the time in hours here: "))
	o=12
	if n>40:
		print("the overtime for worker is",o*(n-40))
	else:
		print("there is not overtime. ")
