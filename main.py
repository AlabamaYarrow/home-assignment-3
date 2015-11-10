# -*- coding: utf-8 -*-

import re
from decimal import Decimal, getcontext
PRECISION = 10


def divide(x, y):
    if y == 0:
        return 'Invalid input'
    else:
        return x / y


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mult(x, y):
    return x * y


def root(x, y):
    getcontext().prec = PRECISION
    if x < 0 or y < 0:
        return 'Invalid input'

    x = Decimal(x)
    y = Decimal(y)
    x0 = x / y
    x1 = 1

    while True:
        x0, x1 = x1, (1 / y)*((y - 1)*x0 + (x / (x0 ** (y - 1))))
        if x0 == x1:
            return x1


def calc(s):
    s = s.replace(' ', '')
    s_split = re.split("([*/+]|--|root)", s)
    try:
        arg1, arg2 = float(s_split[0]), float(s_split[2])
    except ValueError:
        return 'Invalid input'
    operation = s_split[1]

    f = operation_map[operation]

    return f(arg1, arg2)


operation_map = {
    '/': divide,
    '+': add,
    '--': sub,
    '*': mult,
    'root': root
}


def main():
    print 'Operations: '
    print 'Summ: a + b'
    print 'Subtract: a -- b'
    print 'Multiply: a * b'
    print 'Divide: a / b'
    print 'N-th root: a root n'
    print ''

    s = ''
    while s != 'stop':
        s = raw_input('Write expression or \"stop\" to stop: ')
        print calc(s)
    print 'Goodbye!'

if __name__ == '__main__':
    main()
