#!/usr/bin/env python3

# import sympy as sym

def p135(L, D):

    # x = (2u - b) * (2u + b) = c
    n   = sym.Symbol('n', integer=True)
    u   = sym.Symbol('u', integer=True)
    v   = sym.Symbol('v', integer=True)
    eqx = sym.Eq((u + 2*v)**2 - (u+v)**2 - u**2 - n, 0)
    f   = [sym.lambdify([u, n], s) for s in list(sym.solve((eqx), (v, u)))]
    print(list(sym.solve((eqx), (v, u))))

    print(f[1](20, 27))

p135(1e6, 10)
