# -*- coding: utf-8 -*-


def sort_by_merge(array: list) -> list:
    """
    Сортировка слиянием.
    Суть: метод сортирует массив последовательным слиянием пар уже отсортированных подмассивов.
    Сортируемый массив разбивается на две части примерно одинакового размера, затем каждая из получившихся частей
    сортируется отдельно, например — тем же самым алгоритмом. Два упорядоченных массива половинного размера
    соединяются в один и тем самым достигается результат.

    Максимальная временная сложность: О(n*log n)
    Средняя временная сложность: О(n*log n)
    Минимальная временная сложность: О(n*log n)

    Пространственная сложность: О(n)

    (*) Алгоритм устойчивой сортировки.

    :param array: исходный массив
    :return array: упорядоченный исходный массив
    :param array:
    :return:
    """
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        sort_by_merge(left_half)
        sort_by_merge(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i = i + 1
            else:
                array[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            array[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            array[k] = right_half[j]
            j = j + 1
            k = k + 1

    return array
