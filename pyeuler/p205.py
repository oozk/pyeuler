#!/usr/bin/env python3

from itertools import product

def p205():
    dice1, dice2 = range(1, 5), range(1, 7)
    r1, r2 = 9, 6

    peter = {i:0 for i in range(r1, (len(dice1))*r1+1)}
    colin = {i:0 for i in range(r2, (len(dice2))*r2+1)}

    for d in product(dice1, repeat=r1):
        peter[sum(d)] += 1
    for d in product(dice2, repeat=r2):
        colin[sum(d)] += 1

    psum, csum = sum(peter.values()), sum(colin.values())

    result = 0
    for i, c in colin.items():
        result += c / csum * sum(p for j, p in peter.items() if j > i) / psum

    return round(result, 7)

print(p205())
