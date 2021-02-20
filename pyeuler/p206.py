#!/usr/bin/env python3

###
# Problem 206
# https://projecteuler.net/problem=206
###

def p206():
    s = '1_2_3_4_5_6_7_8_9_0'
    match = lambda i : len(str(i)) == len(s) and s.replace('_', '') == "".join(str(i)[2 * x] for x in range(0, 10))
    pool  = reversed(range(int(int(s.replace('_', '0')) ** 0.5), int(int(s.replace('_', '9')) ** 0.5), 10))
    for i in pool:
        if match(i ** 2):
            return i

print(p206())
