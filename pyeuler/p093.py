#!/usr/bin/env python3

###
# Problem 93
# https://projecteuler.net/problem=93
###

from itertools import permutations, product, takewhile

def p093():

    results, maximum, idx = {}, 0, ''

    valid      = lambda n:  n > 0 and n - int(n) == 0
    key        = lambda k: ''.join(str(x) for x in sorted(k))

    digits     = range(1, 10)
    operators  =(lambda a, b: a + b,
                 lambda a, b: a - b,
                 lambda a, b: a * b,
                 lambda a, b: a / b)

    operations = lambda d, o: [o[0]( o[1]( o[2]( d[0], d[1] ), d[2] ), d[3] ),
                               o[0]( o[1]( d[0], d[1] ), o[2]( d[2], d[3] ) )]

    for d in permutations(digits, 4):
        k = key(d)
        for o in product(operators, repeat=3):
            for n in operations(d, o):
                if valid(n):
                    try:
                        results[k].add(int(n))
                    except:
                        results[k] = set()
                        results[k].add(int(n))

    for k in results:
        results[k] = (len(list(takewhile(lambda n: n[1] == n[0] + 1,
                                         enumerate(sorted(results[k]))))),
                      max(results[k]))

    return max(results.items(), key=lambda kv: kv[1]), \
           min(results.items(), key=lambda kv: kv[1]), \
           ('1234', results['1234'])

print(p093())


from itertools import permutations, product, takewhile, zip_longest

def p093_2():

    results    = {}
    output     = {}

    brackets   = ['211', '11(2)', '1(2)1', '1(21)',  '1(1(2))',  '1((2)1)', '(2)11', '(2)0(2)', '(1(2))1', '((2)1)1', '(21)1']
    operations = {'2':' %s %s %s ', '1':' %s %s ', '0':' %s ', '(':'(', ')':')'}
    beautify   = lambda s: ''.join(s).replace('  ', ' ').replace('( ', '(').replace(' )', ')')
    brackets   = [beautify(operations[x] for x in b) for b in brackets]
    operators  = ['+', '-', '*', '/']
    operands   = ['x' + str(x) for x in range(1, 5)]
    placeholdrs= ['%s' for x in range(1, 5)]

    flatten    = lambda l: tuple(x for x in [x for y in l for x in y][:-1])
    lambdify   = lambda eq, o: eval('lambda ' + ','.join(operands) + ': ' + \
                                     eq % flatten(zip_longest(operands, o)))
    stringify  = lambda eq, o: eq.strip() % flatten(zip_longest(placeholdrs, o))
    equations  = [(lambdify(b, o), stringify(b, o)) for o in product(operators, repeat=3) for b in brackets]

    valid      = lambda n:  n > 0 and n - int(n) == 0
    key        = lambda k: ''.join(str(x) for x in sorted(k))
    digits     = range(1, 10)

    for d in permutations(digits, 4):
        k = key(d)
        for eq in equations:
            n = -1
            try:
                n = eq[0](d[0], d[1], d[2], d[3])
            except:
                pass
            if valid(n):
                try:
                    results[k].add((int(n), eq[1] % (d[0], d[1], d[2], d[3])))
                except:
                    results[k] = set()
                    results[k].add((int(n), eq[1] % (d[0], d[1], d[2], d[3])))


    for k in results:
        output[k] = sorted(set(x[0] for x in results[k]))

    for k in output:
        output[k] = (len(list(takewhile(lambda n: n[1] == n[0] + 1,
                                         enumerate(sorted(output[k]))))),
                      max(output[k]))
    idx = max(output.items(), key=lambda kv: kv[1])

    for i in range(1, output[idx[0]][0] + 1):
        for eq in results[idx[0]]:
            if eq[0] == i:
                print(str(eq[0]) + ' = ' + eq[1])

    return idx

print(p093_2())
