# -*- coding: utf-8 -*-

from decimal import Decimal, getcontext
PRECISION = 10


def root(x, y):
    getcontext().prec = PRECISION
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

    s_split = s.split('+')
    if len(s_split) == 2:
        return float(s_split[0]) + float(s_split[1])
    s_split = s.split('-')
    if len(s_split) == 2:
        return float(s_split[0]) - float(s_split[1])
    s_split = s.split('*')
    if len(s_split) == 2:
        return float(s_split[0]) * float(s_split[1])
    s_split = s.split('/')
    if len(s_split) == 2:
        return float(s_split[0]) / float(s_split[1])
    s_split = s.split('root')
    if len(s_split) == 2:
        return root(float(s_split[0]), float(s_split[1]))
    else:
        return 'Invalid input'


def main():
    print 'Operations: '
    print 'Summ: a + b'
    print 'Subtract: a - b'
    print 'Multiply: a * b'
    print 'Divide: a / b'
    print 'N-th root: a root n'
    print ''

    s = ''
    while s != 'stop':
        s = raw_input('Write expression or \"stop\" to stop: ')
        print calc(s)
    print 'goodbye'

if __name__ == '__main__':
    main()
