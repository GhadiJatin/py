import math as m
#m is a alias name of math library
p=float(input("Enter Principal Amount : "))
r=float(input("Enter Rate of Interest : "))
t=int(input("Enter How many years : "))
x=(1+(r/100))
amt=p*m.pow(x,t)
ci=amt-p
print("Amount : ",amt)
print("Compount Interest : ",ci)