# -*- coding: utf-8 -*-
# @Author: SashaChernykh
# @Date:   2023-12-21 10:44:52
# @Last Modified by:   SashaChernykh
# @Last Modified time: 2023-12-21 11:08:26
import datetime
import os
import time

file = ".editorconfig"
print(file)

print("Modified")
print(os.stat(file)[-2])
print(os.stat(file).st_mtime)
print(os.path.getmtime(file))

print()

print("Created")
print(os.stat(file)[-1])
print(os.stat(file).st_ctime)
print(os.path.getctime(file))

print()

modified = os.path.getmtime(file)
print("Date modified: " + time.ctime(modified))
print("Date modified:", datetime.datetime.fromtimestamp(modified))
year, month, day, hour, minute, second = time.localtime(modified)[:-3]
print("Date modified: %02d/%02d/%d %02d:%02d:%02d" %
      (day, month, year, hour, minute, second))

print()

created = os.path.getctime(file)
print("Date created: " + time.ctime(created))
print("Date created:", datetime.datetime.fromtimestamp(created))
year, month, day, hour, minute, second = time.localtime(created)[:-3]
print("Date created: %02d/%02d/%d %02d:%02d:%02d" %
      (day, month, year, hour, minute, second))
