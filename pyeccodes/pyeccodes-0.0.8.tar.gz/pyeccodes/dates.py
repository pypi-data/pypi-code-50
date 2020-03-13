def datetime_to_julian(year, month, day, hour, minute, second):

    dday = float(hour * 3600 + minute * 60 + second) / 86400.0 + day

    if (month < 3):
        y = year - 1
        m = month + 12

    else:
        y = year
        m = month

    a = y // 100

    if y > 1582:
        b = 2 - a + a // 4
    elif y == 1582:
        if (m > 10):
            b = 2 - a + a // 4
        elif m == 10:
            if day > 14:
                b = 2 - a + a // 4
            else:
                b = 0

        else:
            b = 0

    else:
        b = 0

    return (365.25 * (y + 4716)) + int(30.6001 * (m + 1)) + dday + b - 1524.5
