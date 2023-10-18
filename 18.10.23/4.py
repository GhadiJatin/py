#example for global variable 
a=50 #global variable   
def show (): #show() user defined function (no passing argument and no retur value)
    global a
    print("Value of a : ",a)
    #modify the value of global variable a
    a=a+40
    print("After Editing Value of a : ",a)

    


#mainS program
#call function    
show()
print("Value of a : ",a)