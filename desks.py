#!/usr/bin/env python3
# -*- coding: utf-8 -*-

pupils = [int(input()) for i in range(3)]
print(sum([sum(divmod(x, 2)) for x in pupils]))