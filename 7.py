from datetime import date
x=date.today()
print(x)
print(x.strftime("%d-%m-%Y"))
print(x.strftime("%d %B, %Y"))
print(x.strftime("%d %b, %Y"))