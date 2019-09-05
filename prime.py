from math import sqrt
n=int(input("enter the no. here: "))
isprime=True
range=sqrt(n)
div=2
count=1
while div<=range:
	count+=1
	if n%div==0:
		isprime=False
	div+=1
if isprime:
	print("the no. is prime")
else:
	print("the no. is not prime")
print("the total countis :",count)