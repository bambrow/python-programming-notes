#!/usr/bin/env python
# coding:utf-8

import re

'''
^	Matches the beginning of a line
$	Matches the end of the line
.	Matches any character
\s	Matches whitespace
\S	Matches any non-whitespace character
\d  Matches digit
\D  Matches any non-digit character
\w  Matches digit or letter
\W  Matches any non-digit and non-letter character
*	Repeats a character zero or more times
*?	Repeats a character zero or more times (non-greedy)
+	Repeats a character one or more times
+?	Repeats a character one or more times (non-greedy)
?   Repeats a character zero one time
{n} Repeats a character n times
{m-n}   Repeats a character m to n times
[aeiou]	Matches a single character in the listed set
[^XYZ]	Matches a single character not in the listed set
[a-z0-9]	The set of characters can include a range
(	Indicates where string extraction is to start
)	Indicates where string extraction is to end
'''

'''
[0-9a-zA-z\_]   One digit, letter or underscore
[0-9a-zA-z\_]+  String contains multiple digits, letters and/or underscores
[a-zA-z\_][0-9a-zA-z\_]*    String begins with a letter or undercore, and followed by digits, letters and/or underscores
A|B A or B
^\d Begins with digit
\d$ Ends with digit
\s+ One or more white spaces
(...)   Indicates a group, which can be used in .group() or .groups()
'''


def match(regex, text):
    if re.match(regex, text) is not None:
        return True
    else:
        return False

print(match(r'^\d{3}\-\d{3,8}$', '010-12345'))
print(match(r'^\d{3}\-\d{3,8}$', '010 12345'))
print(re.split(r'\s+', 'a  b  c    d   e    f'))
print(re.split(r'[\s\,\;]+', 'a,b  ;c ,;, d ;  e,,,,,f'))
print(match(r'^(\d{3})-(\d{3,8})$', '010-12345'))
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0), m.group(1), m.group(2))
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', '01:54:27')
print(m.groups())
print(re.match(r'^(\d+)(0*)$', '102300').groups())
print(re.match(r'^(\d+?)(0*)$', '102300').groups())

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# compile re in advance, to avoid compiling repeatedly
print(re_telephone.match('010-12345').groups())

m = re.match(r'^(?P<first>\d{3})-(?P<second>\d{3,8})$', '010-12345')
print(m.group('first'), m.group('second'))

print(re.sub('(blue|white|red)', 'black', 'blue sky and white clouds'))
print(re.findall('\d+', '50 students, 12 males, 38 females'))
