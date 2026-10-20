# import calendar
# mon = int(input("enter the month number"))
# year = int(input("enter year"))
# print(calendar.month(year,mon))

# from datetime import datetime
# d = datetime.now()
# print(f"todays date is {d.day}")
# print(f"todays mongth is {d.month}")
# print(f"ongoing year is {d.year}")
# print(f"current time is {d.time}")
# print(f"Hour right now {d.hour}")


from datetime import date,timedelta
datee = int(input("Enter the date "))
month = int(input("enter your month"))
year = int(input("Enyter yiur year"))
dob = date(datee,month,year)

print(f"you date of birth is {dob}")
