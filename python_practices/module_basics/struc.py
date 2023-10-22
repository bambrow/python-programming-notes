#!/usr/bin/env python
# coding:utf-8

import struct

p = struct.pack('>I', 10240099)
print(p)

# > represents big-endian
# I represents unsigned int

u = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
print(u)

# the first 30 bytes of a *.bmp file
s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'

'''
*.bmp file head

2 bytes: 'BM' for Windows, 'BA' for OS/2
4 bytes: file size
4 bytes: reserved bits, 0
4 bytes: offset
4 bytes: bytes of Header
4 bytes: width
4 bytes: height
2 bytes: 1
2 bytes: number of colors
'''

print(struct.unpack('<ccIIIIIIHH', s))



'''
Character	Byte order	Size	Alignment
@	native	native	native
=	native	standard	none
<	little-endian	standard	none
>	big-endian	standard	none
!	network (= big-endian)	standard	none
'''

'''
Format	C Type	Python type	Standard size
x	pad byte	no value
c	char	bytes of length 1	1
b	signed char	integer	1
B	unsigned char	integer	1
?	_Bool	bool	1
h	short	integer	2
H	unsigned short	integer	2
i	int	integer	4
I	unsigned int	integer	4
l	long	integer	4
L	unsigned long	integer	4
q	long long	integer	8
Q	unsigned long long	integer	8
n	ssize_t	integer
N	size_t	integer
f	float	float	4
d	double	float	8
s	char[]	bytes
p	char[]	bytes
P	void *	integer
'''


