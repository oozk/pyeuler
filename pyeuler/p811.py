#!/usr/bin/env python3

from math import comb, floor, log

def p811(t, r, m):

    def A(n):
        def ln(n):
            return floor(log(n, 2))

        def W(n):
            return bin(n).count('1')

        def M(n):
            if n == 0:
                return 1
            else:
                return 5*M(n-1) + 3

        def R(n):
            while n % 2 == 1:
                n >>= 1
            return n

        def B(n):
            return n & -n

        r = R(n)
        b = B(R(n))
        if r == b:
            if b > 0:
                return pow(2, 3*ln(b), m)
            else:
                return 1
        else:
            i = r // b
            return (A(i) * pow(M(W(i)), ln(b), m)) % m

    print('A(81)=', A(81))
    print('A(59049)=', A(59049))
    print('A(1234567)=', A(1234567))
    print('A(123456712345671234567)=', A(123456712345671234567))

    def H(t, r):
        L = []   # Binary Length
        K = []   # Comb(r, k) in binary form
        Z = [0]  # count of zeros
        for k in range(r+1):
            K += [bin(comb(r, k))[2:]]
            L += [k*t]
            if k > 0:
                v = L[-2] + len(K[-2]) - L[-1]
                if v > 0: # Resolve K binary form overlaps
                    K[-1] = bin(int(K[-1], 2) + int(K[-2][:v], 2))[2:]
                    K[-2] = K[-2][v:]
                Z += [ L[-1] - L[-2] - len(K[-2]) ]

        _M = [1]
        c  = sum(k.count('1') for k in K)
        while len(_M) < c+1:
            _M += [ (5*_M[-1] + 3) % m ]

        result = 1
        b1     = 0 # count of ones
        for i in range(len(K)-1, -1, -1):
            k = K[i]
            for j, c in enumerate(k):
                if c == '1':
                    b1 += 1
                if c == '0':
                    result *= _M[b1]
                    result %= m

            if Z[i] > 0:
                result *= pow(_M[b1], Z[i], m)

        return result % m

    return H(t, r)

print(p811(int(1e14+31), 62, int(1e9+62031)))
