#!/usr/bin/env python3

def p297(N):

    fibonacci, sigma_z = [1, 2], [1, 2]
    while fibonacci[-1] < N:
        sigma_z   += [fibonacci[-1] + sigma_z[-1] + sigma_z[-2]]
        fibonacci += [fibonacci[-1] + fibonacci[-2]]

    n = int(N) - 1

    result = 0
    while n > 0:
        i = 0
        while fibonacci[i] <= n: i += 1
        n -= fibonacci[i - 1]
        result += sigma_z[i - 2] + 1 + n
    return result

print(p297(1e17))
