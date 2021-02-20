#!/usr/bin/env python3

import numpy as np
import numba as nb
from scipy.ndimage import label
import multiprocessing as mp
from tqdm import tqdm


solution = 0

# @nb.jit
def add_result(result):
    global solution
    solution += result

# @nb.jit
def p701(n):
    H = W = n
    global solution
    solution = 0
    proc = mp.Pool(mp.cpu_count())
    for i in range(int('1' * H * W, 2)+1):
        # solution += area(i, H, W)
        proc.apply_async(area, args= (i, H, W), callback=add_result)
    proc.close()
    proc.join()
    # for i in sorted(set(solution)):
    #     print(i, solution.count(i))
    return round(solution / (int('1' * H * W, 2) + 1), 8)

# @nb.jit
def area(i, H, W):
    offset = 64 - H * W
    E = np.unpackbits(np.array([i], dtype='>i8').view(np.uint8))
    E = E[offset:].reshape(H, W)
    A = label(E)
    unique, counts = np.unique(A[0], return_counts=True)
    if len(unique) > 1:
        # if max(counts[1:]) == 1:
        #     print(A[0], max(counts[1:]))
        return max(counts[1:])
    elif 1 in unique:
        # print(A[0], max(counts))
        return max(counts)
    else:
        # print(A[0], 0)
        return 0


print(p701(2))
