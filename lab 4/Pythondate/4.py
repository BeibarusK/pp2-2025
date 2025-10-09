from datetime import datetime, timedelta, date

def difference_in_seconds():

    d1 = datetime(2022, 10, 28, 13, 54, 18)
    d2 = datetime(2017, 9, 18, 23, 36, 29)

    time_delta = d1 - d2
    return time_delta.total_seconds()
print(difference_in_seconds())