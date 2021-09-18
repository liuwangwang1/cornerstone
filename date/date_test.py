import datetime

a = datetime.date.today()
# print(a.__getattribute__("year"))
print(a.month)
print(a)
print(a.year)

a = datetime.date(2021, 1, 1)
print(a.isoformat())
print(a.isoweekday())
print(a.weekday())
