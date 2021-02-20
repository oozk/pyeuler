#!/usr/bin/env python3

from itertools import combinations

def p090():
    digits      = (str(x) for x in range(10))
    reversables = [('6', '9'), ('9', '6')]
    squares     = (str(x**2).zfill(2) for x in range(1, 10) if x != 8) #49 reversed to 64

    reversed    = lambda x: (''.join(sorted(x.replace(a, b))) for a, b in reversables)
    pair_dict   = {y:x for x in squares for y in reversed(x)}
    dice_pairs  = lambda d1, d2: set(pair_dict.get(x + y, None) if x < y else \
                                     pair_dict.get(y + x, None) \
                                     for x in d1 for y in d2)
    check_valid = lambda d1, d2: d1 != d2 and len(dice_pairs(d1, d2)) == 9

    dice        = list(combinations(digits, 6))
    return sum(1 for d1 in dice for d2 in dice if check_valid(d1, d2)) // 2

print(p090())
