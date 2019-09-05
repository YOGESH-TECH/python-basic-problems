total=21
while True:
	print("total number of matchstick",total)
	print("user can pick 1 or 2 or 3 and 4 sticks only")
	pick=int(input("enter the pick: "))
	if pick>=1 and pick<=4:
		comppick=5-pick
		print("the computer pick",comppick,'sticks')
		total-=5
	else:
		print("invalid pick try again")
	if total == 1 :
		break 
print("there are remaining only one stick")
print("computer wins")