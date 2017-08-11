# -*- coding: utf-8 -*-
import random
from operator import itemgetter

from by_buble import sort_by_buble
from by_counting import sort_by_counting
from by_extraction import sort_by_extraction
from by_heap import sort_by_heap
from by_inclusion import sort_by_inclusion
from by_merge import sort_by_merge
from by_quick_hoar import sort_by_quick
from by_radix_lsd import sort_by_radix
from by_timsort import sort_by_timsort

BIG_ARRAY = [random.randint(0, 500000) for x in range(1000000)]
RESULT_OUTPUT_FUNC = lambda x, y: '{num}) [{time:0.7f} sec.] {func}'.format(num=y + 1, time=x[0], func=x[1])
FUNC_LIST = [
    sort_by_timsort,
    sort_by_quick,
    sort_by_radix,
    sort_by_merge,
    sort_by_heap,
    sort_by_inclusion,
    sort_by_extraction,
    sort_by_buble,
    sort_by_counting
]


def start_test(array, func_list):
    def get_exec_time(func, array, printResult=False) -> tuple:
        import time

        start_time = time.time()
        print(func(array[:])[:20]) if printResult else func(array[:])
        end_time = time.time() - start_time

        return end_time, func.__name__

    print('-= Start the test: array size of %s elements =-' % len(array))

    result = []
    for x in func_list:
        result.append(get_exec_time(x, array, False))
    result.sort(key=itemgetter(0))

    print('\n'.join(map(RESULT_OUTPUT_FUNC, result, range(len(func_list)))))


def main():
    print('>>> RANDOM:')
    start_test(BIG_ARRAY, FUNC_LIST)

    print('\n>>> SORTED:')
    start_test(sorted(BIG_ARRAY), FUNC_LIST)


if __name__ == '__main__':
    main()
