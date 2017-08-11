# -*- coding: utf-8 -*-


def sort_by_inclusion(array: list) -> list:
    """
    Сортировка простым включением.
    Суть: массив делится на две части - отсортированную и неотсортированную.
    На каждом шаге берется очередной элемент из неотсортированной части и "включается" в отсортированную часть массива.

    Максимальная временная сложность: О(n^2)
    Средняя временная сложность: О(n^2)
    Минимальная временная сложность: О(n)

    Пространственная сложность: О(1)

    (*) Алгоритм НЕ устойчивой сортировки.

    :param array: исходный массив
    :return array: упорядоченный исходный массив
    """
    n = len(array)

    for i in range(n - 1):
        # сохраняем текущий элемент
        temp = array[i + 1]
        # сдвигаем элементы большие чем текущий
        j = i
        while array[j] > temp and j >= 0:
            array[j + 1] = array[j]
            j -= 1
        # вставляем текущий элемент
        array[j + 1] = temp

    return array