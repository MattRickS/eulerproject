named_numbers = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand",
}
named_number_lengths = {num: len(name) for num, name in named_numbers.items()}
joiner = len("and")


def _count_less_one_hundred(n):
    count = 0
    for num, length in sorted(named_number_lengths.items(), reverse=True):
        if n >= num:
            n -= num
            count += length
    return count

HUNDRED = sum(_count_less_one_hundred(i) for i in range(1, 100))


def number_letter_counts():
    count = HUNDRED  # 1-99
    for i in range(1, 10):
        count += (named_number_lengths[i] + named_number_lengths[100]) * 100  # "{N} hundred"
        count += joiner * 99  # "... and ..."
        count += HUNDRED  # 1-99
    
    count += named_number_lengths[1] + named_number_lengths[1000]
    return count


print(number_letter_counts())


# ==============================================================================
# Just for fun, added a way to format any <1m number


def format(n):
    s = ""
    needs_joiner = n > 100
    for num, name in sorted(named_numbers.items(), reverse=True):
        count, n = divmod(n, num)
        if count == 0:
            continue
        
        if num >= 100:
            spacer = " " if s else ""
            s = f"{s}{spacer}{format(count)} {name}"
        elif needs_joiner:
            s = f"{s} and {named_numbers[num]}"
            needs_joiner = False
        elif s:
            s = f"{s} {named_numbers[num]}"
        else:
            s = named_numbers[num]

        if n == 0:
            break
    
    return s
