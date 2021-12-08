import functools

@functools.lru_cache(maxsize=None)
def collatz_length(n):
    if n == 1:
        return 1

    if n % 2 == 0:
        return 1 + collatz_length(n // 2)
    else:
        return 1 + collatz_length(3 * n + 1)


length, i = max((collatz_length(i), i) for i in range(1, 1000000))
print(i)
