x1=int(input("enter the point here: "))
x2=int(input("enter the point here: "))
y1=int(input("enter the point here: "))
y2=int(input("enter the point here: "))
z1=int(input("enter the point here: "))
z2=int(input("enter the point here: "))
r=((y2-x2)/(y1-x1))
s=((z2-y2)/(z1-y1))
if r==s:
	print("lies on same line")
else:
	print("does'nt lieson same line")