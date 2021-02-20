#!/usr/bin/env python3

###
# Problem 61
# https://projecteuler.net/problem=61
###

import networkx as nx

def p061(d):

    #Generate polygonal numbers
    candidates = []
    figurate   = lambda n, s: n * ((s - 2) * n - (s - 4)) // 2
    valid      = lambda p: round(p, d) - int(p) == 0 and len(str(int(p))) == d
    for i in range(1, int((2 * int('9' * d)) ** .5)):
        candidates += [(p, s, n) for p, s, n in [[figurate(i, s), s, i] for s in range(3, 9)] if valid(p)]

    #Generate graph
    shortlist  = lambda x: [p for p in candidates if p[1] == x]
    head, tail = lambda x: str(x[0])[:2], lambda x: str(x[0])[-2:]
    tail2head  = lambda x, j: [p for p in shortlist(j) if tail(x) == head(p)]
    head2tail  = lambda x, j: [p for p in shortlist(j) if head(x) == tail(p)]

    G, edges = nx.DiGraph(), []
    for i in range(8, 2, -1):
        for p in shortlist(i):
            for j in range(3, i):
                for q in tail2head(p, j): edges.append((p, q))
                for q in head2tail(p, j): edges.append((q, p))
    G.add_edges_from(edges)

    #Traverse nodes to find the solution
    def traverse_nodes(G, n, step):
        if step == 0: return [[n]]
        return [[n] + path for node in G.successors(n) \
                           for path in traverse_nodes(G, node, step - 1) \
                           if n not in path]
    seen = []
    for n in G.nodes():
        for cycle in traverse_nodes(G, n, 5):
            if set(x[1] for x in cycle) == set(range(3, 9)) \
               and cycle[0] in [x for x in G.successors(cycle[-1])]:
               if min(x[0] for x in cycle) not in seen:
                   seen.append(min(x[0] for x in cycle))
                   print (sum(x[0] for x in cycle), cycle)

print(p061(6))
