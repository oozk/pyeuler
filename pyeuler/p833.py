#!/usr/bin/env pypy3

def p833(N, M):

    def c(i, P):
        result = 0
        k = 4*i+2
        m = k+1
        A = [0, i, 4*i*(i+1)]
        while A[-1] <= N:
            A += [m*(A[-1]-A[-2])+A[-3]]

        for j, a in enumerate(A[1:]):
            C = []
            n = a*(a+1)//2
            if j == 0:
                c0 = 0
            C  += [k*n-c0]
            C  += [k*C[0]-n]            
            while C[-1] <= N:
                C  += [k*C[-1]-C[-2]]
            c0 = C[0]
            if len([n for n in C if n <= N]) >= 1 and a not in P:
                result += sum(n for n in C if n <= N)
                P      += [a]
        return result, P
    
    Processed = []
    result    = 0 
    for i in range(1, 41017):
        increment, Processed = c(i, Processed)
        result += increment
        Processed = sorted(Processed)

    Processed = sorted(Processed)

    #a(i(k, 1),1)<=1e35 / 1
    f = lambda n, m: (m - n + 1)*(m + n + 1)*(m**2 + 2*m + n**2)//2
    result += f(334370152, 368403149863)

    #a(i(k, 1),2)<=1e35   / 2
    f = lambda n, m: (48*m**5 + 255*m**4 + 475*m**3 + 360*m**2 + 92*m + n*(-48*n**4 - 15*n**3 + 65*n**2 + 15*n - 17))//30
    result += f(5000000, 334370151) #% M

    #a(i(k, 1),3)<=1e35 and a(i(k, 2),1)<=1e35   / 3+1
    f = lambda n, m: (320*m**6 + 1968*m**5 + 4490*m**4 + 4615*m**3 + 2015*m**2 + 242*m - n*(320*n**5 + 48*n**4 - 550*n**3 - 65*n**2 + 230*n + 17))//30
    result += f(303481, 4999999)

    #a(i(k, 1),4)<=1e35 and a(i(k, 2),2)<=1e35  / 4+2
    f = lambda n, m: (3840*m**7 + 28000*m**6 + 78624*m**5 + 105595*m**4 + 67620*m**3 + 16975*m**2 + 486*m + n*(-3840*n**6 - 1120*n**5 + 8736*n**4 + 1925*n**3 - 5880*n**2 - 805*n + 984))//105
    result += f(41017, 303480)

    #remove double counted
    for i in range(41017, 303481):
        k = 4*i*(i+1)
        if k not in Processed and 334370152 <= k <= 368403149863:
            result -= 2*k**3 + 3*k**2 + k

    for k in Processed:
        if 41017 <= k <= 303480:
            result -= 256*k**6 + 832*k**5 + 1024*k**4 + 588*k**3 + 154*k**2 + 14*k
        elif 303481 <= k <= 4999999:
            result -= (64*k**5 + 168*k**4 + 156*k**3 + (119*k**2 + 15*k)//2) 
        elif 5000000 <= k <= 334370151:
            result -= 8*k**4 + 18*k**3 + (25*k**2 + 5*k)//2
        elif 334370152 <= k <= 368403149863:
            result -= 2*k**3 + 3*k**2 + k

    return result % M

print(p833(1e35, 136101521))


from sympy import Symbol, lambdify, solve, expand, Sum
from math import floor
N = 1e100
L = 10
k, n, m = Symbol('k'), Symbol('n'), Symbol('m')

K = [0, k, 4*k*(k+1)]
while len(K) < L:
    K += [expand((4*k+3)*(K[-1]-K[-2])+K[-3])]

A, F = [], []
for i, f in enumerate(K):
    print(i)
    A_  = [expand(f*(f+1)*(2*k+1) - (0 if i == 0 else A[i-1][0]))]
    A_ += [expand((4*k+2)*A_[-1] - f*(f+1)/2)]
    for j in range(L):
        A_ += [expand((4*k+2)*A_[-1] - A_[-2])]
    A += [A_]
    F += [[lambdify(k, f) for f in A_]]


#Solver for intervals
for i, a in enumerate(A[:10]):
    for j, f in enumerate(a[:10]):
        s = solve(f - N, k)
        if len(s) > 0:
            print(i, j, floor(abs(s[0])))

#resulting intervals
#  [((41017, 303480), [(1, 3), (2, 1)]), ((303481, 4999999), [(1, 2), (2, 0)]), 
#  ((5000000, 334370151), [(1, 1)]), ((334370152, 368403149863), [(1, 0)])]

# S = []
# for i in range(1, 3):
#     S_ = []
#     for j in range(4):
#         S_ += [Sum(A[i][j], (k, n, m)).doit()]
#     print(i, j, S_)
#     S += [S_]

# print(expand(S[0][0]+S[0][1]+S[0][2]+S[0][3]+S[1][0]+S[1][1]))
# print(expand(S[0][0]+S[0][1]+S[0][2]+S[1][0]))
# print(expand(S[0][0]+S[0][1]))
# print(expand(S[0][0]))


# from math import floor

# def p833(N, M):

#     def is_square(n):
#         x = n**.5
#         if x - int(x) == 0:
#             return True
#         return False

#     def case2(n):
#         x = floor((n/4)**.5)
#         if n == 4*x*(x+1) and not is_square(n*(n+1)/2):
#             return True
#         return False
    
#     def sum_c1(a):
#         C = []
#         k = 4*a + 2
#         n = a*(a+1)//2
#         C  += [k*n]
#         C  += [k*C[0]-n]
#         while C[-1] <= N:
#             C  += [k*C[-1]-C[-2]]
#         print(a, 'case1', [n for n in C if n <= N])
#         return sum(n for n in C if n <= N) #% M

#     def sum_c2(a):
#         C = []
#         i = floor((a/4)**.5)
#         k = 4*i + 2
#         n = a*(a+1)//2
#         m = i*(i+1)//2
#         C  += [k*(n-m)]
#         C  += [k*C[0]-n]
#         while C[-1] <= N:
#             C  += [k*C[-1]-C[-2]]
#         print(a, 'case2', [n for n in C if n <= N])    
#         return sum(n for n in C if n <= N) #% M

#     a = 1
#     result = 0
#     #Non-square part
#     while (4*a+2)*a*(a+1)//2 <= N:
#         n = a*(a+1)//2
#         if not is_square(n) and not case2(a):
#             result += sum_c1(a)
#             result %= M          
#         a      += 1

#     #Square part
#     G = [0, 6, 210]
#     while G[-1] <= N:
#         G += [35*G[-1]-35*G[-2]+G[-3]]
#     D = [0, 1, 36]
#     while len(D) < len(G):
#         D += [35*(D[-1]-D[-2])+D[-3]]

#     for i, c0 in enumerate(G):
#         C = []
#         if c0 == 0: continue
#         C += [c0]
#         C += [6*C[-1] - D[i]]
#         while C[-1] <= N:
#             C  += [6*C[-1]-C[-2]]
#         a = floor((2*D[i])**.5)
#         print(a, 'case3', [n for n in C if n <= N])
#         result += sum(n for n in C if n <= N) #% M
#         result %= M

#     #Case2 part
#     i = 2
#     a = 4*i*(i+1)
#     increment = sum_c2(a)
#     while increment > 0:
#         if not is_square(a*(a+1)/2):
#             result += increment
#             result %= M
#         i      += 1
#         a = 4*i*(i+1)
#         increment = sum_c2(a)

#     return result #% M

# # print(p833(1e9, 10000000000000000000))


# M = 136101521
# result = 5006553
# f = lambda n, m: (m - n + 1)*(m + n + 1)*(m**2 + 2*m + n**2)//2
# result -= f(6729741224, 368403149863)
# result %= M
# print(result)
from sympy import factorint

def p833_0(S, K, N):

    def issquare(a, b):
        F = {}
        L = [a, a+1, b, b+1]
        for l in L:
            K = factorint(l)
            for k in K.keys():
                try:
                    F[k] += K[k]
                except:
                    F[k]  = K[k]
        r = 1
        f = True
        for k in F.keys():
            if F[k] % 2 == 1:
                f = False
            r *= k ** (F[k]//2)
        return f, r//2

    for a in range(S, K+1):
        for b in range(a+1, int(N)+1):
            f, c = issquare(a, b)
            if f:
                print(a, b, c)

# p833_0(41208, 41209, 1e15)