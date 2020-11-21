from matplotlib import pyplot


x = [1000*i for i in range(1, 6)]
print(x)
y = [
    1.164,
    3.34,
    6.548,
    10.053,
    15.759,
    20.48,
    24.807,
    31.291,
    39.87,
    48.422
]

print(x)
b = [
    4.817,
    51.448,
    217,
    588,
    1325,
]

#pyplot.plot(x, y, '*-')
pyplot.plot(x, b, 'o-')

pyplot.xlabel('Number of digits in an Integer')
pyplot.ylabel('Time/s')
pyplot.show()
