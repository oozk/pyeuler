#!/usr/bin/env python3

###
# Problem 44
# https://projecteuler.net/problem=44
###

import sympy as sym
from tqdm import tqdm

def p044(n):

    pentagon = lambda x: x * (3 * x - 1) / 2

    k = sym.Symbol('k', integer=True)
    j = sym.Symbol('j', integer=True)
    pk = sym.Symbol('pk', integer=True)
    pj = sym.Symbol('pj', integer=True)
    ns = sym.Symbol('ns', integer=True)
    nd = sym.Symbol('nd', integer=True)
    eq1 = sym.Eq(2 * pk - k * (3 * k - 1), 0)
    eq2 = sym.Eq(2 * pj - j * (3 * j - 1), 0)
    eq3 = sym.Eq(2 * pk + 2 * pj - ns * (3 * ns - 1), 0)
    eq4 = sym.Eq(2 * pk - 2 * pj - nd * (3 * nd - 1), 0)
    sols = list(sym.solve((eq1, eq2, eq3, eq4), (pk, pj, ns, nd)))

    funcsum, seen = [], []
    for s in sols:
        if s[2] not in seen:
            seen.append(s[2])
            if sym.lambdify([k, j], s[2])(2, 1) > 0:
                funcsum.append(sym.lambdify([k, j], s[2]))

    funcdiff, seen = [], []
    for s in sols:
        if s[3] not in seen:
            seen.append(s[3])
            if sym.lambdify([k, j], s[3])(2, 1) > 0:
                funcdiff.append(sym.lambdify([k, j], s[3]))

    for ij in tqdm(range(1, n + 1)):
        for ik in range(ij + 1, n + 1):
            if eval_cons(ik, ij, funcsum) and eval_cons(ik, ij, funcdiff):
                return int(pentagon(ik) - pentagon(ij)), (ik, ij)


def eval_cons(ik, ij, functions):

    result = True
    for f in functions:
        a = round(f(ik, ij), 5)
        if a - int(a) != 0:
            result = False
        else:
            return True
    return result

print(p044(3000))
