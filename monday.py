year=int(input("enter the year here: "))
ref_year=1900
diff=year-ref_year
lyear=diff//4
nyear=diff-lyear
td=((nyear*365)+(lyear*366))
day=td%7
if day==0:
	print("monday")
elif day==1:
	print("tuesday")
elif day==2:
	print("wednessday")
elif day==3:
	print("thrusday")
elif day==4:
	print("friday")
elif day==5:
	print("sat.")
elif day==6:
	print("sunday")
else:
	print("error")