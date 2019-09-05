num=int(input("enter the no. here: "))
temp=num
result=""
div=2
while div<=temp:
	if temp%div==0:
		result += " " + str(div) + ", "
		temp=temp//div
	else:
		div=div+1
print(result)