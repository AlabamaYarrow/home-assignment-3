from decimal import Decimal, getcontext
import numbers
PRECISION = 10


getcontext().prec = PRECISION


def are_numeric(*args):
    for arg in args:
        if not isinstance(arg, numbers.Number):
            return False
    return True


def divide(x, y):
    if not are_numeric(x, y):
        return 'Invalid input'
    if y == 0:
        return 'Invalid input'
    else:
        getcontext().prec = PRECISION
        return Decimal(x) / Decimal(y)


def add(x, y):
    if not are_numeric(x, y):
        return 'Invalid input'

    return float(Decimal(x) + Decimal(y))


def sub(x, y):
    if not are_numeric(x, y):
        return 'Invalid input'
    return float(Decimal(x) - Decimal(y))


def mult(x, y):
    if not are_numeric(x, y):
        return 'Invalid input'
    return float(Decimal(x) * Decimal(y))


def root(x, y):
    if not are_numeric(x, y):
        return 'Invalid input'
    if (x < 0 and y % 2 == 0) or y <= 0:
        return 'Invalid input'
    if not isinstance(y, (int, long)):
        return 'Invalid input'

    if x == 0:
        return 0
    x = Decimal(x)
    y = Decimal(y)
    x0 = x / y
    x1 = 1

    while True:
        x0, x1 = x1, (1 / y)*((y - 1)*x0 + (x / (x0 ** (y - 1))))
        if x0 == x1:
            return float(x1)
