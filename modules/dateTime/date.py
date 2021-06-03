import datetime
import pytz

# d = datetime.date(2016, 7, 24)
# print(d)

# Present date
# tday = datetime.date.today()
# print(tday)
# print(tday.year)
# print(tday.month)
# print(tday.day)

# for weekday() Monday 0 Sunday 6
# print(tday.weekday())
# for isoweekday() Monday 1 Sunday 7
# print(tday.isoweekday())

# tdelta = datetime.timedelta(days=7)

# print(tday + tdelta)
# print(tday - tdelta) # this print the date of one week ago

# bday = datetime.date(2021, 6, 13)
# till_bday = bday - tday
# print(till_bday)
# print(till_bday.days)
# print(till_bday.total_seconds())


# t = datetime.time(9, 30, 45, 100000)
# print(t)
# print(t.hour)

# dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 10000)
# print(dt)
# print(dt.date())
# print(dt.time())
# print(dt.year)

# tdelta = datetime.timedelta(days = 7)
# tdelta = datetime.timedelta(hours = 12)
# print(dt + tdelta)

# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()

# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

# dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
# print(dt)
# dt_now = datetime.datetime.now(tz=pytz.UTC)
# print(dt_now)

# dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(dt_utcnow)

# dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)

# dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
# print(dt_mtn)

# for tz in pytz.all_timezones:
# 	print(tz)


# dt_mtn = datetime.datetime.now()
# mtn_zn = pytz.timezone('US/Mountain')

# dt_mtn = mtn_zn.localize(dt_mtn)
# dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
# print(dt_east)
# print(dt_mtn)

dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))
# print(dt_mtn.strftime('%B %d, %Y'))

dt_str = 'May 31, 2021'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

# strftime = Datetime to string
# strptime = String to Datetime