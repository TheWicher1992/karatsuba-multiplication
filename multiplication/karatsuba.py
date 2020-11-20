
from multiplication.add import findSum


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

    e = str(karatsuba(a, c))
    f = str(karatsuba(b, d))
    g = str(karatsuba(b, c))
    h = str(karatsuba(a, d))

    t1 = karatsuba(str(2),str(m))             # 2 * m

    t2 = e.ljust(len(e)+t1,'0')     # 10**(t1)*e

    t3 = findSum(g,h)               # (g+h) 

    t4 = t3.ljust(len(t3)+m,'0')  #(10**m) * (t3)

    t5 = findSum(t2,t4)

    t6 = findSum(t5, f)

    return t6
