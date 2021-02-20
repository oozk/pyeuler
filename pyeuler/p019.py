#!/usr/bin/env python3

###
# Problem 19
# https://projecteuler.net/problem=19
###

def p19(s, e):
    sundays = 0
    months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    leap = lambda m, y : 1 if m == 2 and y % 4 == 0 and ((y % 100 != 0) or (y % 400 == 0)) else 0
    d = 1 + sum(months[m] + leap(m, y) for m in months for y in range(1900, s))
    for y in range(s, e + 1):
        for m in months:
            d += months[m] + leap(m, y)
            if d % 7 == 0:
                sundays += 1
    return sundays

print(p19(1901, 2000))
