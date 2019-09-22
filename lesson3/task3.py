# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
min_value = array[0]
max_value = 0
index_min = 0
index_max = 0
index = 0
for i in array:
    if i < min_value:
        min_value = i
        index_min = index
    if i > max_value:
        max_value = i
        index_max = index
    index += 1

array[index_min], array[index_max] = array[index_max], array[index_min]
print(array)

print(max_value)
print(min_value)
