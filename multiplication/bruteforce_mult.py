from math import floor
from multiplication import add


def brute_mult(x, y):
    lx = len(x)
    ly = len(y)
    result = '0'
    val = ''

    for ix in range(lx-1, -1, -1):
        for iy in range(ly-1, -1, -1):
            val = str(int(x[ix]) * int(y[iy]))
            t1 = val.ljust(len(val) + ((lx - ix - 1) + (ly - iy - 1)), '0')
            result = add.findSum(result, t1)
    return result
