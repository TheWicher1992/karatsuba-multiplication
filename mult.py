from multiplication.karatsuba import karatsuba
from multiplication.bruteforce_mult import brute_mult 
from time import time


i1 = '123456789'
i2 = '987654321'
res = '121932631112635269'

start = time()
assert(karatsuba(i2, i1) == res)
print("Total Time:",time() - start)

start = time()
assert(brute_mult(i2,i1) == res)
print("Total Time:",time() - start)


