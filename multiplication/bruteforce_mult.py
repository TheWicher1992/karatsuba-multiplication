from math import floor
from multiplication.util import add
from multiplication.util import isBigInt


def brute_mult(x, y):
    lx = len(x)
    ly = len(y)
    result = '0'
    val = 0

    for ix in range(lx-1, -1, -1):
        for iy in range(ly-1, -1, -1):
            val = str(int(x[ix]) * int(y[iy]))
            t = val.ljust(len(val) + ((lx - ix - 1) + (ly - iy - 1)),'0')
            result = add(result, t)

    return result
