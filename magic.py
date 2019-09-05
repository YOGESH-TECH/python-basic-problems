n=int(input("enter the no. here: "))
sum=0
while n>0:
	num=n%10
	n=n//10
	sum=sum+num
print("the sum of given no. is: ",sum)

reverse=0
while sum>0:
	new=sum%10
	reverse=(reverse*10)+new
	sum=sum//10
print("the reverse of no. is :",reverse)

a=reverse*sum
if n==a:
	print("the given no. is magic no.")
else:
	print("the given no. is not a magic no.")

	