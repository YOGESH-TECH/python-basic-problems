a=int(input("enter the first no. here: "))
b=int(input("enter the second no. here: "))
if a>b:
	small=b
else:
	small=a
for i in range(1,small+1):
	if b%i==0 and a%i==0:
		hcf=i
		print(hcf)
	else:
		print("error")
	break
c=a*b
lcm=c/hcf
print(lcm)
		