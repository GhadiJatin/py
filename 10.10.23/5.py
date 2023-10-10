mobile=int(input("Enter Mobile No. "))
print("type of mobile : ",type(mobile))
x=len(str(mobile))
#str() inbuilt function , it is used to converts int type data to string type
if x==10:
    print(mobile)
else:
    print("Invalid mobile no.")