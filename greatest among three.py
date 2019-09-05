n1=int(input())
n2=int(input())
n3=int(input())
if n1==n2==n3:
	print("all three are equal")
elif n1<n2<n3:
	print("third is greater")
elif n1>n2>n3:
	print("first is greater")
elif n2>n1>n3:
	print("second is greater")
elif n1==n2>n3:
	print("first and second are largest")
elif n1==n3>n2:
	print("first and third are greatest")
elif n2==n3>n1:
	print("second and third are greatest")
elif n2==n3<n1:
	print("first is largest")
elif n1==n3<n2:
	print("second is largest")
elif n1==n2<n3:
	print("third is largest")
else:
	print("error")