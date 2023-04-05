#!/usr/bin/env python3

from itertools import product
def p821(n):
    R = list(range(1, 4))
    D = [p for p in product(R, R, R, R, R)]
    w1, w2 = 0, 0
    for car1 in D:
        round = False
        for car2 in D:
            d1, d2 = 0, n
            if round:
                round = False
                continue
            for i in range(len(car1)):
                d1 += car1[i]
                if d1 > d2:
                    # print(car1, car2, '1')
                    w1 += 1
                    round = True
                    break
                d2 += car2[i]
                if d2 > d1:
                    print(car1, car2, '2')
                    w2 += 1
                    round = True
                    break
    t = w1+w2
    print(t, w1, w2, w1/t, w2/t, w1/t-w2/t, 2/11)

print(p821(2))
