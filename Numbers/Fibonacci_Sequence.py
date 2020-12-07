def fib(num):
    if num in (1, 2):
        return 1
    return fib(num - 1) + fib(num - 2)


while True:
    try:
        number = int(input('Enter No. of Fibonacci sequence:'))
        if number < 0:
            print('Please, enter nonnegative value')
            continue
    except ValueError:
        print('Please, enter a number')
    else:
        print(fib(number))
        break
