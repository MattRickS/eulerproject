def pythagorean_triplet(n):
    squares = {}
    for c in range(1, n):
        c_squared = c * c
        for b_squared in squares:
            a = squares.get(c_squared - b_squared)
            if a is None:
                continue

            b = squares[b_squared]
            if a + b + c == n:
                return a, b, c

        squares[c_squared] = c


a, b, c = pythagorean_triplet(1000)
print(a * b * c)
