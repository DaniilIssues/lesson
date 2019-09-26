# Определить, какое число в массиве встречается чаще всего.

import random
import cProfile

SIZE = 300
MIN_ITEM = -100
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


# Вариант1
# def freq_array(array):
#     spam = []
#     for i in array:
#         spam.append(array.count(i))
#
#     return array[max(spam)]

# "task1.freq_array([random.randint(0, 100) for _ in range(100)])"
# 100 loops, best of 5: 536 usec per loop
# "task1.freq_array([random.randint(0, 100) for _ in range(200)])"
# 100 loops, best of 5: 1.64 msec per loop
# "task1.freq_array([random.randint(0, 100) for _ in range(300)])"
# 100 loops, best of 5: 3.32 msec per loop
# "task1.freq_array([random.randint(0, 100) for _ in range(400)])"
# 100 loops, best of 5: 5.56 msec per loop
# 100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects} // 100
# 100    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
# 200    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects} // 200
# 200    0.001    0.000    0.001    0.000 {method 'count' of 'list' objects}

# Вариант2
# def freq_array2(array):
#     n = 0
#     item = array[0]
#     for i in array:
#         m = 0
#         for q in array:
#             if i == q:
#                 m += 1
#         if m > n:
#             item = i
#             n = m
#     return item
# "task1.freq_array2([random.randint(0, 200) for _ in range(100)])"
# 100 loops, best of 5: 728 usec per loop
# "task1.freq_array2([random.randint(0, 200) for _ in range(200)])"
# 100 loops, best of 5: 2.46 msec per loop
# "task1.freq_array2([random.randint(0, 200) for _ in range(300)])"
# 100 loops, best of 5: 5.16 msec per loop
# "task1.freq_array2([random.randint(0, 200) for _ in range(400)])"
# 100 loops, best of 5: 8.95 msec per loop
# 1    0.001    0.001    0.001    0.001 task1.py:35(freq_array2) // 100
# 1    0.002    0.002    0.002    0.002 task1.py:35(freq_array2) // 200
# 1    0.005    0.005    0.005    0.005 task1.py:35(freq_array2) // 300

# Вариант3
# def freq_array3(array):
#     spam = {i: array.count(i) for i in array}
#     for k, v in spam.items():
#         if v == max(spam.values()):
#             return k


# "task1.freq_array3([random.randint(0, 200) for _ in range(100)])"
# 100 loops, best of 5: 564 usec per loop
# "task1.freq_array3([random.randint(0, 200) for _ in range(200)])"
# 100 loops, best of 5: 1.72 msec per loop
# "task1.freq_array3([random.randint(0, 200) for _ in range(300)])"
# 100 loops, best of 5: 3.45 msec per loop
# "task1.freq_array3([random.randint(0, 200) for _ in range(400)])"
# 100 loops, best of 5: 5.74 msec per loop
# 100    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects} // 100
#   1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
#   8    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
# 200    0.001    0.000    0.001    0.000 {method 'count' of 'list' objects} // 200
#   1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
#   9    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
# 300    0.003    0.000    0.003    0.000 {method 'count' of 'list' objects} // 300
#   1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
#   7    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}

# Вывод:
# Все алгоритмы примерно одинаковы, линейной сложности, поэтому сложно выбрать из них лучший,
# но судя по timeit первый вариант работает быстрее, поэтому пусть он будет лучшим.

