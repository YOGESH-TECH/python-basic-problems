n=int(input("enter the no. here: "))
def lst_n(n):
	while n>=10:
		n=n//10
	return n
def frst_1(n):
	n=n%10
	return n
print("the lastno. is: ",lst_n(n))
print("the first no. is: ",frst_1(n))
sum1=lst_n(n)+frst_1(n)
print("the first sum is: ",sum1)

n=n//10
sum2=0
while n>=10:
	num=n%10
	n=n//10
	sum2=sum2+num
print("the second sum is: ",sum2)


if sum1==sum2:
	print("cool")
else:
	print("not cool")