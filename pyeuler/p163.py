#!/usr/bin/env python3

def p163(n):

    return int((1678 * n ** 3 + 3117 * n ** 2 + 88 * n \
             - 345 * (n % 2) \
             - 320 * (n % 3) \
             -  90 * (n % 4) \
             - (n ** 3 - n ** 2 + n) % 5 * 288) / 240)

print(p163(36))


# import itertools
# n = 36
# all_segs = set((1.0, 0.0, float(n)/2.0) for n in xrange(1, 2*n))
# all_segs |= set((0.0, 1.0, float(n)) for n in xrange(0, n))
# all_segs |= set((1.0, 1.5, float(n)) for n in xrange(1, 2*n))
# all_segs |= set((2.0, 1.0, (float(n)+1.0)*2.0) for n in xrange(0, n))
# all_segs |= set((1.0, -1.5, float(n)) for n in xrange(1-n, n))
# all_segs |= set((2.0, -1.0, float(n)*2.0) for n in xrange(0, n))
# print len(all_segs)
#
# def too_close(p1, p2):
#   return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 < 1e-10
#
# def intersect(eq1, eq2):
#   (a1, b1, c1) = eq1
#   (a2, b2, c2) = eq2
#   if (a1, b1) == (a2, b2):
#     return None
#   y = (c1 * a2 - c2 * a1) / (b1 * a2 - b2 * a1)
#   x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
#   if y < -1e-5 or y - 2.0*x > 1e-5 or 2.0*x + y > 2.0*n + 1e-5:
#     return None
#   return (x, y)
#
# nb = 0
# nb_total = 0
# for (eq1, eq2, eq3) in itertools.combinations(all_segs, 3):
#   nb_total += 1
#   x12 = intersect(eq1, eq2)
#   x13 = intersect(eq1, eq3)
#   x23 = intersect(eq2, eq3)
#   if x12 == None or x13 == None or x23 == None:
#     continue
#   if too_close(x12, x23) or too_close(x12, x13) or too_close(x13, x23):
#     continue
#   nb += 1
#
# print (nb, nb_total)
