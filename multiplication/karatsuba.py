from multiplication.util import add
from multiplication.util import sub


def karatsuba(x, y):
    lx = len(x)
    ly = len(y)

    if lx < 2 or ly < 2:
        return str(int(x) * int(y))
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
    g = karatsuba(add(a, b), add(c, d))

    t1 = e.ljust(len(e) + (2*m), '0')   # 10**(2*m)*e

    t2 = sub(g, add(f, e))        # g - f - e

    t3 = t2.ljust(len(t2) + m, '0')     # 10**m*(g - f - e)

    t4 = add(t3, f)                 # 10**m*(g - f - e) + f

    t5 = add(t1, t4)                # 10**(2*m)*e + 10**m*(e + f - g) + f

    return t5
