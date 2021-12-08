def fibonnaci(a, b):
    n = a + b
    if n <= 4000000:
        yield n
        yield from fibonnaci(b, n)


if __name__ == "__main__":
    print(2 + sum(n for n in fibonnaci(1, 2) if n % 2 == 0))
