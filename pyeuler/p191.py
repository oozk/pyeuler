#!/usr/bin/env python3

import numpy as np

def p191(L):
    T = np.matrix([[1, 1, 1, 0, 0, 0],
                   [1, 0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0, 0],
                   [1, 1, 1, 1, 1, 1],
                   [0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 1, 0]])

    T = T ** L
    return sum(T * np.matrix([[1]] + [[0]]*5))

print(p191(4))


    # return sum(T**30 *np.matrix('1;0;0;0;0;0'))
    # forfeit = lambda x: x.count('L') > 1 or 'AAA' in x
    # cases   = ['L', 'O', 'A']
    # cases   = [''.join(s) for s in product(cases, repeat=15) if not forfeit(s)]
    #
    # L       = [lambda x: 'L' in x, lambda x: not 'L' in x]
    # sA      = [lambda x: x[0] == 'A' and x[1] != 'A', \
    #            lambda x: x[0] != 'A', \
    #            lambda x: x[:2] == 'AA']
    # eA      = [lambda x: x[-1] == 'A' and x[-2] != 'A', \
    #            lambda x: x[-1] != 'A', \
    #            lambda x: x[-2:] == 'AA']
    #
    # C       = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    # for x in cases:
    #     for i, l in enumerate(L):
    #         for j, s in enumerate(sA + eA):
    #             if l(x) and s(x): C[i][j] += 1
    # result   = C[0][3]*(C[1][0]+C[1][1]) +  C[0][4]*(sum(C[1][:3])) + C[0][4]*C[1][1]
    # # result  *= 2
    # return result
