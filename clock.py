#!/usr/bin/env python3
# -*- coding: utf-8 -*-

minutes_total = int(input('Enter minutes: '))
hours, minutes = divmod(minutes_total, 60)
if hours >= 24:
    hours %= 24
print('{}:{}'.format(hours, minutes))