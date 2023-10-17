#4. Default argument 
def addition(a=0,b=0,c=0,d=0): 
    return a+b+c+d

#main program
result=addition(2,3) #sum of 2 nos.
print("Sum of 2 nos. : ",result)

result=addition(20,30,40) #sum of 3 nos.
print("Sum of 3 nos. : ",result)

result=addition(20,30,40,50) #sum of 4 nos.
print("Sum of 4 nos. : ",result)