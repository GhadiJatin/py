n=int(input("How many students : "))
i=1 #initial first student
while i<=n: #outer loop
    name=input("Enter Name of Student :")
    print("Name :",name)
    j=1 # initial marks of first subject
    while j<=3 : #inner loop
        marks=int(input("Enter Marks of students : "))
        print("Marks of {} subjects of {} student {}".format(j,i,marks))
        j=j+1 #increment inner loop
        i=i+1 #increment outer loop