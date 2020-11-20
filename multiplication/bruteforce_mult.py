from math import floor
def brute_mult(x,y):
    lx = len(x)
    ly = len(y)
    result = 0
    val = 0
    
    for ix in range(lx-1,-1,-1):
        for iy in range(ly-1,-1,-1):
            val = int(x[ix]) * int(y[iy])
            result = result + (int(val)) * ( 10 ** ((lx - ix - 1) + (ly - iy - 1)))
    return result
