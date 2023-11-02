with open("test.txt","r+") as f:
    print(f.read())
    f.write("something sensible")
    f.seek(0)
    print(f.read())
