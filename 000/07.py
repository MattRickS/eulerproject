import math


def is_prime(n):
    return all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))


def nth_prime(n):
    count = 1
    i = 1
    while count < n:
        i += 2
        if is_prime(i):
            count += 1

    return i


print(nth_prime(10001))
