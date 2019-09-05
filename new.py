x=int(input("enter here the total no.s:  "))
count=0
doo=0
tri=0
for i in range(1,x+1):
	n=int(input("enter here: "))
	if n>0:
		count+=1
		continue
	elif n<0:
		doo+=1
		continue
	elif n==0:
		tri+=1
		continue
print('the no.of are',count)
print('the no.of negative are',doo)
print('the no.of zero are',tri)
