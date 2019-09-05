from math import pow
for i in range(1,2001):
	org=i
	sum=0
	while org>0:
		new=org%10
		t=pow(new,3)
		sum=sum+t
		org=org//10
	if i==sum:
		print(i)
