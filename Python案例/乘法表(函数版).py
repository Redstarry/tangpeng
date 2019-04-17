#!/user/bin/env python3


def MutiplicationTable(number):
    '''
    此函数是乘法表，可以实现任何位数的乘法表。
    :param number: 这是一个数字，表示几以内的乘法表，例如：九九乘法表，number = 10；
    :return:此函数没有返回值。
    '''
    for x in range(1, number):
        for y in range(1, x + 1):
            print('%d * %d = %2d' % (y, x, x * y), end='  ')
        print('')

