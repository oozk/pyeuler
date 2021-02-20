#!/usr/bin/env python3

###
# Problem 79
# https://projecteuler.net/problem=79
###


keylog = '''
319
680
180
690
129
620
762
689
762
318
368
710
720
710
629
168
160
689
716
731
736
729
316
729
729
710
769
290
719
680
318
389
162
289
162
718
729
319
790
680
890
362
319
760
316
729
380
319
728
716
'''

from constraint import *

def p079(keylog, i):

    log = [[x for x in k] for k in keylog.strip().splitlines() if len(k) > 0][:i]
    keys = sorted(set(x for l in log for x in l))
    positions = [(x[j], x[i]) for x in log for i in range(len(x)) for j in range(i+1,len(x))]

    problem, solutions = Problem(), set()
    for k in keys: problem.addVariable(k, range(len(keys)))
    for (i, j) in set(positions): problem.addConstraint(lambda a, b: a > b, (i, j))
    for s in problem.getSolutions(): solutions.add(''.join(x[0] for x in sorted(s.items(), key=lambda i: i[1])))

    return(solutions)

def p079_2(keylog):
    from itertools import permutations

    log  = [[x for x in k] for k in keylog.strip().splitlines() if len(k) > 0]
    keys = sorted(set('x%s' % x for l in log for x in l))
    cons = set('x%s < x%s' % (x[i], x[j]) for x in log for i in range(len(x)) \
                                                       for j in range(i+1,len(x)))
    vars = lambda p: ('global %s; %s = %s' % (v, v, i) for i, v in enumerate(p))
    sols = set()

    for p in permutations(keys):
        for v in vars(p): exec(v)
        if all(eval(c) for c in cons):
            sols.add(''.join(p).replace('x', ''))

    return(sols)

def p079_3(keylog):
    import networkx as nx

    log = [[x for x in k] for k in keylog.strip().splitlines() if len(k) > 0]
    positions = set((x[i], x[j]) for x in log for i in range(len(x)) for j in range(i+1, len(x)))

    edges = list()
    for p in positions: edges.append(p)
    graph = nx.DiGraph()
    graph.add_edges_from(edges)

    return ''.join(nx.topological_sort(graph))

# print(p079(keylog, 50))
print(p079_2(keylog))
# print(p079_3(keylog))
