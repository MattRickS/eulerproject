import math


def is_prime(value):
    return all(value % i != 0 for i in range(2, int(math.sqrt(value)) + 1))


def highest_prime(value):
    last_prime = None
    for i in range(2, int(math.sqrt(value)) + 1):
        factor, remainder = divmod(value, i)
        if remainder != 0:
            continue
        elif is_prime(factor):
            return factor
        elif is_prime(i):
            last_prime = i

    return last_prime


if __name__ == "__main__":
    print(highest_prime(600851475143))
