#datetime inbuilt function in python
#datetime means 10/16/223 4:08:23
#format for datetime mm/dd/yyyy hh:mm:ss

#to show current date and time  : use inbuilt method now ()

from datetime import date as d
print("Current date : ",d.today())

#To show only current time /system time 
from datetime import datetime as d
x=d.now()  #system date and time 
#inbuilt method strftime("%H:%M:%S")
t=x.strftime("%H:%M:%S")
print("Current time : ",t)

print("System date and time : ",x)
#to extract year of current date and time
y=x.year #year inbuilt attribute
print("Year of system date : ",y)