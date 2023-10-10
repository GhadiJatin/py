pinno=2568 #original pin no
i=0
while i<3:
    pin=int(input("Enter pin no. of your card : "))
    if pin==pinno:
        #process
        print("Valid Pin no")
        print("Transaction successfully complted")
        break #exit from loop
    else:
        print("Invalid pin no. ")
        i=i+1
        print("Attempt No. : ",i)

    print("Ghari Ja")