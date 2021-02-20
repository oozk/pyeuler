def p710():
  n = 2
  while n <= 50:
      n += 2
      print(n, t(n))
      # if t(n) % 1e6 == 0:
      #     return n

def t(n):
  mid_idx = n // 2
  result = (1, ) * mid_idx
  c = 0
  for i in range(0, 2 ** mid_idx):
      r = ('0' * mid_idx + bin(i)[2:])[-mid_idx:]
      if r[:2] == '10' or r[-2:] == '01' or '010' in r:
          c += 1
          #print(r)
  return c

p710()
