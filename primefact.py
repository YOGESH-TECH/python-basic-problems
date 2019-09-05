num=int(input("enter the no. here: "))
div=2
while div<=num:
	if num%div==0:
		num=num/div
		print(int(div))
		num=num
	else:
		div=div+1
		
		