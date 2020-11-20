from multiplication import add


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

    e = str(int(karatsuba(a, c)))
    f = str(int(karatsuba(b, d)))
    g = str(int(karatsuba(b, c)))
    h = str(int(karatsuba(a, d)))

    # return 10**(2*m)*e + 10**m*(g+h) + f
   # print(e, f, g, h)
    t1 = 2*m            # 2 * m

    t2 = e.ljust(len(e)+t1, '0')     # 10**(t1)*e

    t3 = add.findSum(g, h)               # (g+h)

    t4 = t3.ljust(len(t3)+m, '0')  # (10**m) * (t3)

    t5 = add.findSum(t2, t4)

    t6 = add.findSum(t5, f)

    return t6
