#4 example for variable length Arguments :-
#WAP to find the sum of n nos.
def addition(*x):
    s=0
    for i in x:
        s=s+i
    return s

#main program
result=addition(10,20) #sum of 2 nos.
print("Sum of 2 nos. : ",result)

result=addition(10,20,30,) #sum of 3 nos.
print("Sum of 3 nos. : ",result)

result=addition(3,4,5,6) #sum of 4 nos.
print("Sum of 4 nos. : ",result)