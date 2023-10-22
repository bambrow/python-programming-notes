#!/usr/bin/env python
# coding:utf-8

from PIL import Image, ImageFilter

im = Image.open('test.jpg')
w, h = im.size
print('Image size: {0} * {1}'.format(w, h))
im.thumbnail((w//2, h//2))
print('Image resized to: {0} * {1}'.format(w//2, h//2))
im.save('test_thumbnail.jpg', 'jpeg')

im2 = Image.open('test.jpg')
im3 = im2.filter(ImageFilter.BLUR)
im3.save('test_blur.jpg', 'jpeg')
