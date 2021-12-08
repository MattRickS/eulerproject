month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

year = 1900  # 1-based
month = 0  # 0-based
day = 6  # 0-based, starting on a Sunday

def get_month_days():
    if month == 1 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return 29
    return month_days[month]

num_sunday_firsts = 0

while year < 2001:
    day += 7
    count, day = divmod(day, get_month_days())
    month += count
    count, month = divmod(month, len(month_days))
    year += count
    if 1900 < year < 2001:
        num_sunday_firsts += int(day == 0)

print(num_sunday_firsts)
