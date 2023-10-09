p=int(input("Enter Principal : "))
r=int(input("Enter Rate of Interest : "))
t=int(input("Enter Time Period : "))
si=(p*r*t/100)
amt=p+si
#print("Simple Interest=",si, "\nAmount :",amt)
print("Simple Interest :.{}\nAmount .{}".format(si,amt))
#\n new line : inbuilt command of py
