#!/usr/bin/env python
# coding:utf-8

from datetime import datetime, timedelta, timezone

print(datetime.now())
print(datetime(2016, 12, 20, 7, 10))
print(datetime.now().timestamp())
print(datetime(2016, 12, 20, 7, 10).timestamp())

print(datetime.fromtimestamp(1073741824.0))
print(datetime.fromtimestamp(2147483648.0))
print(datetime.utcfromtimestamp(2147483648.0))

print(datetime.strptime('2016-12-20 07:10:00', '%Y-%m-%d %H:%M:%S'))
print(datetime.now().strftime('%a, %b %d %H:%M:%S'))

t = datetime.now()
print(t + timedelta(hours=10))
print(t - timedelta(minutes=100))

utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)

'''
datetime module directives

%a	Weekday as locale’s abbreviated name.
%A	Weekday as locale’s full name.
%w	Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.	0, 1, ..., 6
%d	Day of the month as a zero-padded decimal number.	01, 02, ..., 31
%b	Month as locale’s abbreviated name.
%B	Month as locale’s full name.
%m	Month as a zero-padded decimal number.	01, 02, ..., 12
%y	Year without century as a zero-padded decimal number.	00, 01, ..., 99
%Y	Year with century as a decimal number.	0001, 0002, ..., 2013, 2014, ..., 9998, 9999
%H	Hour (24-hour clock) as a zero-padded decimal number.	00, 01, ..., 23
%I	Hour (12-hour clock) as a zero-padded decimal number.	01, 02, ..., 12
%p	Locale’s equivalent of either AM or PM.
%M	Minute as a zero-padded decimal number.	00, 01, ..., 59
%S	Second as a zero-padded decimal number.	00, 01, ..., 59
%f	Microsecond as a decimal number, zero-padded on the left.	000000, 000001, ..., 999999
%z	UTC offset in the form +HHMM or -HHMM (empty string if the object is naive).	(empty), +0000, -0400, +1030
%Z	Time zone name (empty string if the object is naive).	(empty), UTC, EST, CST
%j	Day of the year as a zero-padded decimal number.	001, 002, ..., 366
%U	Week number of the year (Sunday as the first day of the week) as a zero padded decimal number.
    All days in a new year preceding the first Sunday are considered to be in week 0.	00, 01, ..., 53
%W	Week number of the year (Monday as the first day of the week) as a decimal number.
    All days in a new year preceding the first Monday are considered to be in week 0.	00, 01, ..., 53
%c	Locale’s appropriate date and time representation.
%x	Locale’s appropriate date representation.
%X	Locale’s appropriate time representation.
%%	A literal '%' character.	%
'''

