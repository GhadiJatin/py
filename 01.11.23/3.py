f=open('test.txt')
text=f.readline()
while text:
    print(text)
    text=f.readline()
    
f.close()
