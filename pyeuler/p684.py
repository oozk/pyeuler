def f(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def S(n, m):
    p = n // 9
    r = n % 9
    return ((6 + (r + 3) * r / 2) * pow(10, p, m) - 9 * p - r - 6) % m

def p684(ls, le, mod):
    return(sum(S(i, mod) for i in f(le)[ls:]) % mod)

print(p684(2, 90, int(10 ** 9 + 7)))
