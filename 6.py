from datetime import date
#to find the age of given date 
yr=int(input("Enter Year : "))
mn=int(input("Enter Month : "))
day=int(input("Enter Date : "))
dob=date(yr,mn,day)
print(type(dob))
#extract year from system date
y1=date.today().year
#find the age
age=y1-yr
print("Age : ",age)