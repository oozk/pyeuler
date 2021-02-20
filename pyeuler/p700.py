def eulercoin():
    f = 1504170715041707
    m = 4503599627370517
    l = []
    n = 1
    c = f * n % m
    while c not in l:
        l.append(c)
        n += 1
        print(n)
        c = f * n % m

    return len(l)

print(eulercoin())
