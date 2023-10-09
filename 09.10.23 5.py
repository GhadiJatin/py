i=1 #initial value for line
while i<=5: #outer loop for line
    j=1 #initial value for column
    while j<=i: #inner loop for column
        print("*",end="")
        j=j+1 #increment column j by 1
    i=i+1 #increment line i by 1
    print() #go to new line
