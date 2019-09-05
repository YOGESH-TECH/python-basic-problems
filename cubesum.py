from math import pow
num=int(input("enter the no. here: "))
org=num
sum=0
for i in range(1,501):
	new=num%10
	t=pow(new,3)
	sum=sum+t
	num=num//10
	i+=1
print("the sum of the given no. is",int(sum))
y=int(sum)
if org==y:
	print("the given no. is armstrong")
else:
	print("not armstrong")