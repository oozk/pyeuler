def p076(n):
    coins = range(1, n)
    ways = [1] + [0] * n
    for c in coins:
        for i in range(n - c + 1):
            ways[i + c] += ways[i]
    return ways[n]

print(p076(100))
