def lattice(n):
    """
    Solution used. Each point on the grid is the sum of the number of ways to
    reach the points above and to the left. Because the grid is symmetrical,
    the middle diagonal will always be the sum of identical values.
    """
    grid = [[1] * (i + 1) for i in range(n + 1)]
    for y in range(1, n + 1):
        for x in range(1, y + 1):
            if x == y:
                val = grid[y][x - 1] * 2
            else:
                val = grid[y - 1][x] + grid[y][x - 1]
            grid[y][x] = val

    return grid[-1][-1]


def lattice(n):
    """
    Alternate solution discovered from the comments. Math is crazy.
    """
    import math
    return math.comb(n * 2, n)


print(lattice(20))
