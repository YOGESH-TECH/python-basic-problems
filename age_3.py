age1=int(input("enter the age of Ram here: "))
age2=int(input("enter the age of Shyam here: "))
age3=int(input("enter the age of Ajay here: "))
if age1>age2>age3:
	print("Ajay is youngest.")
elif age2>age3>age1:
	print("Ram is youngest.")
elif age1>age3>age2:
	print("Shyam is youngest.")
elif age1==age2>age3:
	print("Ajay is youngest.")
elif age1==age3>age2:
	print("Shyam is youngest.")
elif age2==age3>age1:
	print("Ram is youngest.")
elif age2==age3==age1:
	print("all three are of same age")
else:
	print(error)