result=""
first = 0
second=1

count=1
while count<=15:
	result+="[" +str(first)+"]"
	next=first+second
	first=second
	second=next
	count+=1
	
print(result)