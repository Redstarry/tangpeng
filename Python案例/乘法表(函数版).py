#!/user/bin/env python3
'''
    乘法表的进阶函数版；
    multiplication_table(number) 表示number以内的乘法表；
    九九乘法表的时候，number = 10
'''

def MutiplicationTable(number):
    for x in range(1, number):
        for y in range(1, x + 1):
            print('%d * %d = %2d' % (y, x, x * y), end='  ')
        print('')

MutiplicationTable(10)