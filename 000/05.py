import math


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def smallest_multiple():
    # All values <11 can be divided into the values >10
    val = 11
    for i in range(12, 21):
        val = lcm(val, i)
    return val


print(smallest_multiple())
