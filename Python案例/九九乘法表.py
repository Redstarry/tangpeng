#!/user/bin/env python3

'''
    学习Python For循环的时候写的简单的案例

'''

for x in range(1, 10):
    for j in range(1, x + 1):
        print('%d * %d = %2d' % (j, x, x * j), end='  ')
    print('')