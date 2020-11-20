
def karatsuba(x, y):
    lx = len(x)
    ly = len(y)

    if lx < 2 or ly < 2:
        return int(x) * int(y)
    n = lx

    if(ly > lx):
        x = x.zfill(ly)
        n = ly
    if(lx > ly):
        y = y.zfill(lx)
        n = lx

    m = int(n/2)

    a = x[0:n-m]
    b = x[n-m:n]
    c = y[0:n-m]
    d = y[n-m:n]

    e = karatsuba(a, c)
    f = karatsuba(b, d)
    g = karatsuba(b, c)
    h = karatsuba(a, d)
    return 10**(2 * m)*e + (10**m) * (g+h) + f
