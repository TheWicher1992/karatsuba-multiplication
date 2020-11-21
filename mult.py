from multiplication.karatsuba import karatsuba
from multiplication.bruteforce_mult import brute_mult



type_of_mult = input().upper()
x = input()
y = input()

try:
    answer = brute_mult(x,y) if type_of_mult == 'B' else karatsuba(x,y)
    print(answer)
except: 
    print("Error in input format")


