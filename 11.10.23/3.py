#isalpha() means check alphabets only (a-z or A-Z) if only alphabets return
#True otherwise return False
userid=input("Enter Userid , please enter only alphabets and number both")
if(userid.isalpha()):
    password=input("Enter Password : ")
    print("Successfully Login")
    print("User Id : ",userid)
    print("password : ",password)
else:
    print("Invalid user id , please enter only aplphabets and number")    