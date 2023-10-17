#3. Default Argument and retrun value 
def addition_2(a,b): #addition of 2 nos.
    return a+b

def addition_3(a,b,c): #addition of 3 nos.
    return a+b+c
def addition_4(a,b,c,d): #additio of 4 nos.
    return a+b+c+d

#main program
print("1. su of 2 nos.")
print("2. sum of 3 nos.")
print("3. sum of 4 nos.")
ch = int(input("Enter Your choice : "))
if ch==1:
    a=float(input("Enter First Number : "))
    b= float(input("Enter Second number :"))
    #call function
    result=addition_2(a,b)
    print("Sum of two numbers ",result)
elif ch==2:
    a=float(input("Enter first Number."))
    b=float(input("Enter Second Number :"))
    c=float(input("Enter Third Number"))
    #call function
    result=addition_3(a,b,c)
    print("Sum of three numbers ",result)
elif ch==3:
    a=float(input("Enter first Number."))
    b=float(input("Enter Second Number :"))
    c=float(input("Enter Third Number : "))
    d=float(input("Enter Fourth Number : "))
    #call function
    result=addition_4(a,b,c,d)
    print("Sum of three numbers ",result)
else:
    print("Invalid Choice")




