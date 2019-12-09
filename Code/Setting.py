#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Times   : 2019/11/21 8:55
# @Author  : zwj
# @Email   : zhangwj18@shanghai-electric.com
# @File    : __init__.py
# @Project: PyCharm

import urllib
import string
import datetime
import time

# a = "16  #"
#
# print(urllib.parse.quote(a,safe=string.printable))

# print(time.strptime("2019-10-01", "%d/%m/%Y"))
print(len([1,2,3]))
print(datetime.datetime.strptime("2019-10-01","%Y-%m-%d").strftime("%y/%m/%d"))
print(type(datetime.datetime.strptime("2019-10-01","%Y-%m-%d")))
print ('%.2f' %(int("32")))

