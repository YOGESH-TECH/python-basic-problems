p=int(input("enter the cost price here: "))
s=int(input("enter the selling price here: "))
if s-p>0:
	print("profit made is: ",s-p)
elif s-p<0:
	print("loss made is: ",p-s)
else:
	print("nor loss neither profit")