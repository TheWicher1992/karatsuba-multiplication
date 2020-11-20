from math import floor
def add(x,y):
    lx = len(x)
    ly = len(y)
    n = lx
    if(ly > lx):
        x = x.zfill(ly)
        n = ly
    if(lx > ly):
        y = y.zfill(lx)
        n = lx
    
    result = ''
    r = 0
    q = 0
    for i in range(n - 1, -1, -1):
        val = int(x[i]) + int(y[i]) + q
        r = int(val % 10)
        q = floor(val / 10)
        if i == 0:
            result = str(val) + result
            break
        result = str(r) + result
    
    return result


 

