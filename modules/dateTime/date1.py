import datetime
import time

# t = datetime.time(1, 2, 3)
# print(t)
# print("hour :", t.hour)
# print("minute :", t.minute)
# print("second :", t.second)
# print("microsecond :", t.microsecond)
# print('tzinfo :', t.tzinfo)

# The min and max class attributes reflect the valid range of times
# in a single day.
# print("Earliest :", datetime.time.min)
# print('Latest :', datetime.time.max)
# print('Resolution :', datetime.time.resolution)

# The resolution for time is limited to whole microseconds.
# for m in [1, 0, 0.1, 0.6]:
# 	try:
# 		print("{:02.1f}".format(m), datetime.time(0, 0, 0, microsecond=m))
# 	except TypeError as err:
# 		print("ERROR:", err)
# Floating point values for microseconds cause a TypeError.

# today = datetime.date.today()
# print(today)
# print('ctime :', today.ctime())
# tt = today.timetuple()
# print('tuple : tm_year =', tt.tm_year)
# print('	  : tm_mon  =', tt.tm_mon)
# print('	  : tm_mday  =', tt.tm_mday)
# print('	  : tm_hour  =', tt.tm_hour)
# print('	  : tm_min  =', tt.tm_min)
# print('	  : tm_sec  =', tt.tm_sec)
# print('	  : tm_wday  =', tt.tm_wday)
# print('	  : tm_yday  =', tt.tm_yday)
# print('	  : tm_isdst  =', tt.tm_isdst)
# print('ordinal:', today.toordinal())
# print('Year :', today.year)
# print('Mon :', today.month)
# print('Day :', today.day)

# o = 733114
# print('o   :', o)
# print('fromordinal(o)  :', datetime.date.fromordinal(o))

# t = time.time()
# print('t   :', t)
# print('fromtimestamp(t):', datetime.date.fromtimestamp(t))

# print('Earliest :', datetime.date.min)
# print('Latest :', datetime.date.max)
# print("Resolution :", datetime.date.resolution)

# new date instances uses the replace() method of an existing
# date.

# d1 = datetime.date(2008, 3, 29)
# print("d1:", d1.ctime())

# d2 = d1.replace(year = 2009)
# print('d2:', d2.ctime())

# Future and past dates can be calculate using basic arithmetic
# on two datetime objects, or by combining a datetime with timedelta.

# print('microseconds:', datetime.timedelta(microseconds = 1))
# print('microseconds:', datetime.timedelta(microseconds = 1))
# print('seconds :', datetime.timedelta(seconds = 1))
# print('seconds:', datetime.timedelta(seconds = 1))
# print('minute :', datetime.timedelta(minutes = 1))
# print('hours :', datetime.timedelta(hours = 1))
# print('days :', datetime.timedelta(days = 1))
# print('weeks :', datetime.timedelta(weeks=1))

# Date math uses the standard arithmetic operators.

# today = datetime.date.today()
# print("Today :", today)

# one_day = datetime.timedelta(days=1)
# print('one day :', one_day)

# yesterday = today - one_day
# print('yesterday :', yesterday)

# tomorrow = today + one_day
# print('Tomorrow :', tomorrow)

# print()
# print('tomorrow - yesterday', tomorrow - yesterday)
# print('yesterday - tomorrow', yesterday - tomorrow)

# one_day = datetime.timedelta(days=1)
# print('1 day :', one_day)
# print('5 days :', one_day * 5)
# print('1.5 days :', one_day * 1.5)
# print('1/4 days : ', one_day / 4)

# # assume an hour for lunch
# work_day = datetime.timedelta(hours = 7)
# meeting_length = datetime.timedelta(hours=1)
# print('meetings per day :', work_day / meeting_length)

# Both date and time values can be compared using the standard
# comparison operators to determine which is earlier or later.

# print('Times: ')
# t1 = datetime.time(12, 55, 0)
# print(' t1:', t1)
# t2 = datetime.time(13, 5, 0)
# print(' t2 :', t2)
# print(' t1 < t2:', t1 < t2)

# print()
# print("Dates: ")
# d1 = datetime.date.today()
# print(' d1:', d1)
# d2 = datetime.date.today() + datetime.timedelta(days=1)
# print(' d2:', d2)
# print(' d1 > d2:', d1 > d2)

# print('Now  :', datetime.datetime.now())
# print('Today :', datetime.datetime.today())
# print('UTC Now :', datetime.datetime.utcnow())
# print()

# FIELDS = [
# 	'year', 'month', 'day',
# 	'hour', 'minute', 'second',
# 	'microsecond',
# ]

# d = datetime.datetime.now()
# for attr in FIELDS:
# 	print("{:15}: {}".format(attr, getattr(d, attr)))

# t = datetime.time(1, 2, 3)
# print('t :', t)

# d = datetime.date.today()
# print('d :', d)

# dt = datetime.datetime.combine(d, t)
# print('dt:', dt)

# The defaultstring representation of a datetime object uses the ISO-8601
# format (YYYY-MM-DDTHH:MM:SS.mmmmmm). Alternate formats can be generated using
# strftime().

# format = "%a %b %d %H:%M:%S %Y"

# today = datetime.datetime.today()
# print("ISO :", today)

# s = today.strftime(format)
# print('strftime :', s)

# d = datetime.datetime.strptime(s, format)
# print('strptime :', d.strftime(format))

# today = datetime.datetime.today()
# print('ISO  :', today)
# print('format() : {:%a %b %d %H:%M:%S %Y}'.format(today))

min6 = datetime.timezone(datetime.timedelta(hours=-6))
plus6 = datetime.timezone(datetime.timedelta(hours=6))
d = datetime.datetime.now(min6)

print(min6, ":", d)
print(datetime.timezone.utc, ':', d.astimezone(datetime.timezone.utc))
print(plus6, ':', d.astimezone(plus6))

# convert to the current system timezone
d_system = d.astimezone()
print(d_system.tzinfo,'	:', d_system)
