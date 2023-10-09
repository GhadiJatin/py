# Percentage
rno=int(input("Enter Roll No. : "))
name=input("Enter Student Name : ")
a=float(input("Enter marks of sub1 : "))
b=float(input("Enter marks of sub2 : "))
c=float(input("Enter marks of sub3 : "))
d=float(input("Enter marks of sub4 : "))
e=float(input("Enter marks of sub5 : "))
#find the total marks
total=a+b+c+d+e
print("Total Marks : ",total)

#find the percentage
per=total*100/500
print("Percentage : ",per)
if(per>=85):
    grade="A+"
elif(per<85 and per>=70):
    grade="A"
elif(per<70 and per>=60):
    grade="b"
else:
    grade="c"
print("Grade:",grade)
