import datetime

# 1.convert a string to datetime.
date_T = datetime.datetime.strptime('Aug 28 2018 2:43PM', '%b %d %Y %I:%M%p')
print(date_T)

# 2.subtract five days from current date.

a_date = datetime.datetime.now()
days = datetime.timedelta(5)

date = a_date - days
print(" a subtract of 5 days from a current date", date)


# 3. convert the date to datetime.
def date_time():
    dt = datetime.datetime.combine(date.today(), datetime.time())
    print("date to datetime", dt)


date_time()

# 4. next 7 days starting from today
print("next 7 days from today date ")
base = datetime.datetime.today()
for a in range(0, 8):
    print("->", base + datetime.timedelta(days=a))
