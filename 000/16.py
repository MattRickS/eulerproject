def power_digit_sum(n):
    return sum(map(int, str(1 << n)))


print(power_digit_sum(1000))
