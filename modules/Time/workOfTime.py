# Implementation details for the clocks varies by platform. Use get_clock_info
# () to access basic information about the current implementation, including
# the clock’s resolution.
import hashlib
import textwrap
import time
import os
# available_clocks = [
#     ('monotonic', time.monotonic),
#     ('perf_counter', time.perf_counter),
#     ('process_time', time.process_time),
#     ('time', time.time),
# ]

# for clock_name, func in available_clocks:
#     print(textwrap.dedent('''\
#     {name}:
#         adjustable    : {info.adjustable}
#         implementation: {info.implementation}
#         monotonic     : {info.monotonic}
#         resolution    : {info.resolution}
#         current       : {current}
#     ''').format(
#         name=clock_name,
#         info=time.get_clock_info(clock_name),
#         current=func())
#     )

# time() returns the number of seconds since the strart of the 
# "epoch" as a floating point value

# The epoch is the start of measurement for time, which for Unix systems is 0:00
# on January 1, 1970. Although the value is always a float, actual precision is
# platform-dependent.

# print("The time is :", time.time())

# ctime() can be more useful to make time readable

# print('The time is :', time.ctime())
# later = time.time() + 15
# print('15 secs from now :', time.ctime(later))

# start = time.monotonic()
# time.sleep(0.1)
# end = time.monotonic()
# print('start : {:>9.2f}'.format(start))
# print('end : {:>9.2f}'.format(end))
# print('span :{:>9.2f}'.format(end - start))

# While time() returns a wall clock time, process_time() returns processor clock
# time. The values returned from process_time() reflect the actual time used by
# the program as it runs.

# data to use to calculate md5 checksums
# data = open(__file__, 'rb').read()

# for i in range(5):
# 	h = hashlib.sha1()
# 	print(time.ctime(), ':{:0.3f} {:0.3f}'.format(
# 		time.time(), time.process_time()))
# 	for i in range(300000):
# 		h.update(data)
# 	cksum = h.digest()

# template = '{} - {:0.2f} - {:0.2f}'

# print(template.format(
#     time.ctime(), time.time(), time.process_time())
# )

# for i in range(3, 0, -1):
#     print('Sleeping', i)
#     time.sleep(i)
#     print(template.format(
#         time.ctime(), time.time(), time.process_time())
#     )


# Data to use to calculate md5 checksums
# data = open(__file__, 'rb').read()

# loop_start = time.perf_counter()

# for i in range(5):
#     iter_start = time.perf_counter()
#     h = hashlib.sha1()
#     for i in range(300000):
#         h.update(data)
#     cksum = h.digest()
#     now = time.perf_counter()
#     loop_elapsed = now - loop_start
#     iter_elapsed = now - iter_start
#     print(time.ctime(), ': {:0.3f} {:0.3f}'.format(
#         iter_elapsed, loop_elapsed))


# def show_struct(s):
# 	print('	tm_year  :', s.tm_year)
# 	print('	tm_mon :', s.tm_mon)
# 	print(' tm_mday :', s.tm_mday)
# 	print('	tm_hour :', s.tm_hour)
# 	print(' tm_min :', s.tm_min)
# 	print(' tm_sec :', s.tm_sec)
# 	print(' tm_wday :', s.tm_wday)
# 	print(' tm_yday :', s.tm_yday)
# 	print(' tm_isdst :', s.tm_isdst)

# print('gmtime:')
# show_struct(time.gmtime())
# print('\nlocaltime:')
# show_struct(time.localtime())
# print('\nmktime:', time.mktime(time.localtime()))

# def show_zone_info():
# 	print('	TZ  :', os.environ.get('TZ', '(not set)'))
# 	print(' tzname :', time.tzname)
# 	print('	Zone : {} ({})'.format(
# 			time.timezone,(time.timezone / 3600)))
# 	print('	DST :', time.daylight)
# 	print('	Time :', time.ctime())
# 	print()

# print("Default :")
# show_zone_info()

# ZONES = [
# 	'GMT',
# 	'Europe/Amsterdam',
# ]

# for zone in ZONES:
# 	os.environ['TZ'] = zone
# 	# time.tzset()
# 	print(zone, ':')
# 	show_zone_info()

def show_struct(s):
    print('  tm_year :', s.tm_year)
    print('  tm_mon  :', s.tm_mon)
    print('  tm_mday :', s.tm_mday)
    print('  tm_hour :', s.tm_hour)
    print('  tm_min  :', s.tm_min)
    print('  tm_sec  :', s.tm_sec)
    print('  tm_wday :', s.tm_wday)
    print('  tm_yday :', s.tm_yday)
    print('  tm_isdst:', s.tm_isdst)


now = time.ctime(1483391847.433716)
print('Now:', now)

parsed = time.strptime(now)
print('\nParsed:')
show_struct(parsed)

print('\nFormatted:',
      time.strftime("%a %b %d %H:%M:%S %Y", parsed))