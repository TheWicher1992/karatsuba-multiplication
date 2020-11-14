from math import floor, ceil


def karatsuba(x, y, n):
    if n == 1:
        return x * y

    m = ceil(n / 2)

    a = floor(x / 10**m)
    b = x % 10**m

    c = floor(y / 10**m)
    d = y % 10**m

    e = karatsuba(a, c, m)
    f = karatsuba(b, d, m)

    g = karatsuba(b, c, m)
    h = karatsuba(a, d, m)

    return int(10**(2*m)*e + 10**m * (g + h) + f)


def karatsuba_mult(x, y):

    n = len(x) if len(x) >= len(y) else len(y)
    return karatsuba(int(x), int(y), n)


def naive_mult(x, y):
    return "to be implemented"


def multiply(t, x, y):
    if t == 'D':
        return naive_mult(x, y)
    elif t == 'B':
        return karatsuba_mult(x, y)


def main():
    #t = input("Enter type:")
    x = input("Enter first number:")
    y = input("Enter second number:")
    print(karatsuba_mult(x, y))
    #print(multiply(t, x, y))


if __name__ == "__main__":
    main()
