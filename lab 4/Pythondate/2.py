from datetime import date, timedelta

x=date.today()

y=x-timedelta(days=1)
print(y)
print(x)

z=x+timedelta(days=1)
print(z)