num=int(input("enter the no. here: "))
sum=0
while num>0:
	new=num%10
	print(new,"+",end=" ")
	sum=sum+new
	num=num//10
print("=",sum) 