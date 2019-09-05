n=int(input("enter the no. here: "))
def frst_d(n):
	while n>=10:
		n=n//10
	return n

def lst_d(n):
	n=n%10
	return n
print("the first digit is: ",frst_d(n))
print("the last digit is: ",lst_d(n))
sum=frst_d(n)+lst_d(n)
print("the sum of first and last digit is: ",sum)
