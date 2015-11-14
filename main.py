# -*- coding: utf-8 -*-

import re
from calc import divide, add, sub, mult, root


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
