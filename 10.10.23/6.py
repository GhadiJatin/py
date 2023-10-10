mobile=input("Enter Mobile No. ")
if(mobile.isdigit ()):
    print("type of mobile : ",type(mobile))
    mobile=int(mobile)
    print("type of mobile : ",type(mobile))
else:
    print("Please enter integer value") 

 #isdigit() : return answer True/False
 #isdigit() inbuilt string functionn , it is  used to check given input is digit
 #or not (0-9)