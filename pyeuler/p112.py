#!/usr/bin/env python3

def p112(target):

    increasing = lambda n: all(n[i+1] >= n[i] for i in range(len(n)-1))
    decreasing = lambda n: all(n[i] >= n[i+1] for i in range(len(n)-1))
    bouncy     = lambda n: not increasing(n) and not decreasing(n)

    n, b, r = 1, 0, 0
    while r < target:
        if bouncy(str(n)):
            if increasing(str(n)[:-1]):
                j = int(str(n)[-2:-1]) - int(str(n)[-1:])
                # print(n, j, r)
                # break
            if decreasing(str(n)[:-1]):
                j = 9 - int(str(n)[-2:-1]) - int(str(n)[-1:])
                # print(n, j, r)
                # break
            if j > 0 and r < target - .01:
                b += j + 1
                n += j
                r = b / n
                n += 1
                print(n, b, j, r)
                # break
            else:
                b += 1
                n += 1
                # break

            if n == 538:
                print(n, r)
                break

        else:
            n += 1

    return n

print(p112(.5))
