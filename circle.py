import math
a=int(input("enter the center x here: "))
b=int(input("enter the center y here: "))
r=int(input("enter the radius here: "))
c=int(input("enter the given x here: "))
d=int(input("enter the given y here: "))
t=math.sqrt((math.pow(c-a,2)+math.pow(d-b,2)))
if t==r:
	print("the point lies on the circle")
elif t>r:
	print("the point is outside the circle")
elif t<r:
	print("the point is inside the circle.")
else:
	print("something went wrong:")