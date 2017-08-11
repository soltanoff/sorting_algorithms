# -*- coding: utf-8 -*-
from math import log


def sort_by_radix(array: list, base=10) -> list:
    """
    Поразрядная сортировка least significant digit (LSD).
    Суть: Числа сортируются по разрядам, сначала сортируются младшие разряды, затем старшие. При LSD сортировке
    олучается следующий порядок: короткие ключи идут раньше длинных, ключи одного размера сортируются по алфавиту, это
    совпадает с нормальным представлением чисел: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.

    Максимальная временная сложность: О(nk)
    Средняя временная сложность: О(nk)
    Минимальная временная сложность: О(nk)

    Пространственная сложность: О(k)

    (*) Алгоритм устойчивой сортировки.

    :param array: исходный массив
    :return array: упорядоченный исходный массив
    """

    def getDigit(num, base, digit_num):
        # pulls the selected digit
        return (num // base ** digit_num) % base

    def makeBlanks(size):
        # create a list of empty lists to hold the split by digit
        return [[] for i in range(size)]

    def split(a_list, base, digit_num):
        buckets = makeBlanks(base)
        for num in a_list:
            # append the number to the list selected by the digit
            buckets[getDigit(num, base, digit_num)].append(num)
        return buckets

    def merge(a_list):
        # concatenate the lists back in order for the next step
        new_list = []
        for sublist in a_list:
            new_list.extend(sublist)
        return new_list

    def maxAbs(a_list):
        # largest abs value element of a list
        return max(abs(num) for num in a_list)

    def split_by_sign(a_list):
        # splits values by sign - negative values go to the first bucket,
        # non-negative ones into the second
        buckets = [[], []]
        for num in a_list:
            if num < 0:
                buckets[0].append(num)
            else:
                buckets[1].append(num)
        return buckets

    # there are as many passes as there are digits in the longest number
    passes = int(round(log(maxAbs(array), base)) + 1)
    new_list = list(array)
    for digit_num in range(passes):
        new_list = merge(split(new_list, base, digit_num))

    return merge(split_by_sign(new_list))
