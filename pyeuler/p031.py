def p031(n):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [1] + [0] * n
    for c in coins:
        for i in range(n - c + 1):
            ways[i + c] += ways[i]
    return ways[n]

print(p031(200))
