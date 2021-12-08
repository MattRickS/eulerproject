value = 1
for i in range(2, 101):
    value *= i

print(sum(map(int, str(value))))
