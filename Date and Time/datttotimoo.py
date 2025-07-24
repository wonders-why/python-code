import datetime

x = datetime.datetime.now()# to print the date and time
print(x)

x = datetime.date.today() # to print the date
print(x)

x = datetime.datetime(2025,11,20) #to print the date and time you set yourself
print(x)# prints the date
print(x.year)# prints the year
print(x.month)#prints the month
#date isnt aviable

print(x.strftime("%A")) #strftime funtion is used to print string names of months like sunday monday and other 
#there are plenty of other notations like %A to print diffrent things in diffrent ways all mentioned in strftime.txt in the same folder