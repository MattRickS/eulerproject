def largest_palindrome():
    highest = 1
    # There are palindromes in the 9XXXX9 range, which can only be achieved
    # with factors >900.
    for a in range(999, 900, -1):
        for b in range(999, 900, -1):
            x = a * b
            s = str(x)
            if s == s[::-1]:
                highest = max(highest, x)

    return highest


print(largest_palindrome())
