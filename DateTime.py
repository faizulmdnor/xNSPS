import datetime
x = datetime.datetime.now()
print(x)
print(x.strftime("%d %B, %Y"))
print(x.strftime("%H%M")),
print(x.strftime("%z"))

udate = input("Date of Born (DD/MM/YYYY): " )

day,month,year = udate.split('/')
isValidDate = True
try:
    datetime.datetime(int(year),int(month),int(day))
except ValueError:
    isValidDate = False
if(isValidDate):
    print("date is valid: ", udate)
else:
    print("Date is not valid: ", udate)
