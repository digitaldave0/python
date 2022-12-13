import datetime


#print datetime
x = datetime.datetime.now()
print(x)

#print day, year
x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))


#print define, year,month,day
x = datetime.datetime(2020, 5, 17)
print(x)

#display month
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))

