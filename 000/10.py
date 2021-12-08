import math


def sieve_of_eratosthenes(n):
    values = [True] * (n + 1)
    sqrt = int(math.sqrt(n))
    for i in range(2, sqrt + 1):
        if values[i]:
            yield i
            for j in range(i*i, n+1, i):
                values[j] = False

    for x in range(sqrt, n + 1):
        if values[x]:
            yield x


print(sum(sieve_of_eratosthenes(2000000)))
