#sum of no. between the first and the last.
n=int(input("enter the no. here: "))
n=n//10
def sum_1(n):
	sum=0
	while n>=10:
		num=n%10
		n=n//10
		sum=sum+num
	return sum
print(sum_1(n))
