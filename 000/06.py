def triangle_number(n):
    return n * (n + 1) // 2


def sum_of_squares(n):
    return sum(i * i for i in range(1, n + 1))


def square_of_sum(n):
    x = triangle_number(n)
    return x * x


def sum_square_difference(n):
    return square_of_sum(n) - sum_of_squares(n)


print(sum_square_difference(100))
