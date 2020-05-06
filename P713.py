#!/usr/bin/env python3

###
# Problem 713
# https://projecteuler.net/problem=713
###
# Solution: O(n) time | O(1) space
###

import cProfile

def L(N):
    return sum(T(N, m) for m in range(2, N + 1))

def T(N, m):

    partitions  = m - 1
    part1_size  = N // partitions
    part2_size  = part1_size + 1
    part2_count = N - part1_size * partitions
    part1_count = partitions - part2_count

    choose_2 = lambda n : int(n * (n-1) / 2)

    return part1_count * choose_2(part1_size) + part2_count * choose_2(part2_size)

class memoize: #decorator
	def __init__(self, func):
		self.func = func
		self.cache = {}

	def __call__(self, *args):
		if args in self.cache:
			return self.cache[args]
		else:
			value = self.func(*args)
			self.cache[args] = value
			return value
@memoize
def T_recursive(N, m):
    #initial naive idea on T function, O(n^2) time
    if m == 2:              # N choose 2
        return int(N * (N - 1) / 2)

    if m > N // 2 + 1:      # m > N/2 : pick 2 new at a time until success
        return N - m + 1

    if m <= N // 2 + 1:     # if 2 < m <= N/2 then pick the best out of all possible partitions
        return min(T_recursive(N-i, m-1) + T_recursive(i, 2) for i in range(2, N-1))


print(T(3, 2))
print(T(8, 4))
cProfile.run('print(L(int(1e7)))')
