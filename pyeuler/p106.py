from math import factorial

def p106(n):

    n_choose_r   = lambda n, r: factorial(n) / factorial(r) / factorial(n-r)
    totaltests   = lambda n: sum(n_choose_r(n, i) *  n_choose_r(n - i, j)
                                                        for i in range(1, n)
                                                        for j in range(1, n - i + 1)) // 2
    equalitytest = lambda i: n_choose_r(i, i//2) // 2 - n_choose_r(i, i // 2) // (i // 2 + 1)
    eqtestcount  = lambda n: sum(n_choose_r(n, i) * equalitytest(i) for i in range(4, n + 1, 2))

    # print('Set Size      : %s ' % n)
    # print('Subset Pairs  : %s ' % totaltests(n))
    # print('Equality Tests: %s ' % eqtestcount(n))

    return totaltests(n)

# # p106(4)
# # p106(7)
# p106(12)

for i in range(1, 30):
    print(p106(i))
