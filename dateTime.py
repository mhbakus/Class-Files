import datetime

'''
DateTime is combinaison of date and time
Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.
'''
print "Current date and time: " , datetime.datetime.now()

'''
TIME
functions time define the time
first argument the hour,
second the minutes
third the seconds
'''

time = datetime.time(3, 24, 00)
print(time)

'''
date(year, month, day) --> date object
DATE
Calendar date values are represented with the date class
argument year, month, day
current date today()
'''

today = datetime.date.today()
print(today)

'''
TimeDelta
A timedelta object represents a duration, the difference between two dates or times.
'''

delta = str(datetime.date.today() + datetime.timedelta(days=15, hours=85, minutes=15, seconds=5))
print(delta)


