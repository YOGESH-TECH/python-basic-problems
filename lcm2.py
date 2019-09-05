from math import gcd
n1=int(input("enter the first no. here: "))
n2=int(input("enter the second no. here: "))
a=gcd(n1,n2)
b=(n1*n2)/a

print("hcf is:",a)
print("lcm is.:",b)