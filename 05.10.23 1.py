#WAP to check the given quatdratic equation are real , eqal or imaginary
a=float(input("Enter number a : "))
b=float(input("Enter number b : "))
c=float(input("Enter number c : "))
#find the discriminant d=b*b-4*a*c
d=b*b-4*a*c
print("Discriminant : ",d)
if(d>0):
    print("Real root")
elif(d==0):
    print("Equal root")
else:
    print("Imaginary root")
