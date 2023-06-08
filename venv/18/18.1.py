def is_leap_year(x):
    if not x % 400 or not x % 4 and x % 100:
        return True
    else:
        return False

print(is_leap_year(1704))