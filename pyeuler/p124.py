#!/usr/bin/env python3

import numpy as np
import pandas as pd

def p124_2(lim, k):

    R = np.ones(lim, dtype=int)
    N = np.arange(1, lim + 1)
    for i in range(2, lim):
        if R[i - 1] == 1:
            R[i - 1 :: i] *= i

    E = pd.DataFrame(R, columns=["rad(n)"])
    E["n"] = N
    E.sort_values(by=["rad(n)", "n"], inplace=True)

    return E.iloc[[k - 1]]

print(p124_2(100000, 10000))
