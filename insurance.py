age=int(input("enter the age of person here: "))
sex=str(input("enter the sex here:"))
area=str(input("enter the area here:"))
amount=int(input("enter the amount in thousand: "))
health=str(input("enter the health of the person: "))

if 25<=age<=35:
	if sex=='male':
		if area=='city' and health=='good':
			premium=4*amount
			if premium<=200000:
				print("the premium amount is rs.",premium)
			else:
				print("not eligible")
		elif area=='village' and health=='poor':
			premium=6*amount
			if premium<=100000:
				print("the premium amount is rs.",premium)
			else:
				print("not eligible")
	elif sex=='female':
		if area=='city' and health=='good':
			premium=3*amount
			if premium<=100000:
				print("the premium is rs.",premium)
			else:
				print("not eligible")
	else:
		print("wrong sex.")
else:
	print("can not be insured")
		
	