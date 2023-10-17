#2.Keyword Arguments/parameters and return value


def interest(x,y,z): # x=principal , y=rate of interest , z=time

    s=x*y*z/100
    a=s+x
    return s,a




#main program
p=float(input("Enter Principal Amount : "))
r=float(input("Enter Rate of Interest : "))
t=int(input("Enter How Many Years : "))
#call function
si,amt=interest(y=r,x=p,z=t)#here p,r and t are actual parameter 
print("Simple interest",si)
#call function

print("Amount",amt)
