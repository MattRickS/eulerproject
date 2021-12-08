import math


def factor_count(n):
    return sum(2 for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0)


def divisible_triangle_number(n):
    num = 1
    triangle = 1
    while True:
        num += 1
        triangle += num
        if factor_count(triangle) >= n:
            return triangle


print(divisible_triangle_number(500))
