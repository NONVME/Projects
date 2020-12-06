from decimal import Decimal
from math import pi as constant

MAX_LIMIT = len(str(Decimal(constant))) - 1


def limit_decimal(num, limit):
    return f'The meaning of PI: {num:.{limit}f}'


while True:
    try:
        limit = (int(input(
            "Please, enter the maximum number of decimal places for PI: ")))
        if limit >= MAX_LIMIT:
            print(f'Enter a number smaller than {MAX_LIMIT}.')
            continue
        elif limit < 0:
            print('Please, enter nonnegative value')
            continue
    except ValueError:
        print('Please, enter a number')
    else:
        print(limit_decimal(constant, limit))
        break
