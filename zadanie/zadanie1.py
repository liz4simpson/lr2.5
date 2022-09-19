#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = ()
    b = ()
    a_li = list(a)
    b_li = list(b)

    n = int(input('Введите количество элементов кортежа: '))
    print('Ведите элементы списка:\n')
    for i in range(n):
        a_li.append(int(input()))
        if (i+1) % 2 == 0:
            b_li.append(a_li[i]**2)
        else:
            b_li.append(a_li[i]*2)
    a = tuple(a_li)
    b = tuple(b_li)
    print('a = ', a, '\nb = ', b)