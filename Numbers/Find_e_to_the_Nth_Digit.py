from decimal import Decimal
from math import e as constant

MAX_LIMIT = len(str(Decimal(constant))) - 1


def limit_decimal(num, limit):
    return f'The meaning of e: {num:.{limit}f}'


while True:
    try:
        limit = (int(input(
            "Please, enter the maximum number of decimal places for e: ")))
        if limit >= MAX_LIMIT:
            print(f'Enter a number smaller than {MAX_LIMIT}.')
            continue
        elif limit <= 0:
            print('Please, enter positive value')
            continue
    except ValueError:
        print('Please, enter a number')
    else:
        print(limit_decimal(constant, limit))
        break
