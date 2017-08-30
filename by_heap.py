# -*- coding: utf-8 -*-


def sort_by_heap(array: list) -> list:
    """
    Пирамидальная сортировка.
    Суть: Сортировка пирамидой использует бинарное сортирующее дерево. Выстраиваем элементы массива в виде сортирующего
    дерева, затем будем удалять элементы из корня по одному за раз и перестраивать дерево. То есть на первом шаге
    обмениваем Array[1] и Array[n], преобразовываем Array[1], Array[2], … , Array[n-1] в сортирующее дерево.
    После чего переставляем Array[1] и Array[n-1], преобразовываем Array[1], Array[2], … , Array[n-2] в сортирующее
    дерево. Процесс продолжается до тех пор, пока в сортирующем дереве не останется один элемент. Тогда Array[1],
    Array[2], … , Array[n] — упорядоченная последовательность.

    Максимальная временная сложность: О(n*log n)
    Средняя временная сложность: О(n*log n)
    Минимальная временная сложность: О(n*log n)

    Пространственная сложность: O(1)

    (*) Алгоритм НЕ устойчивой сортировки.

    :param array: исходный массив
    :return array: упорядоченный исходный массив
    """
    def swap(i, j):
        array[i], array[j] = array[j], array[i]

    def heapify(end, i):
        l = 2 * i + 1
        r = 2 * (i + 1)
        max = i
        if l < end and array[i] < array[l]:
            max = l
        if r < end and array[max] < array[r]:
            max = r
        if max != i:
            swap(i, max)
            heapify(end, max)

    end = len(array)
    start = end // 2 - 1
    for i in range(start, -1, -1):
        heapify(end, i)
    for i in range(end-1, 0, -1):
        swap(i, 0)
        heapify(i, 0)

    return array