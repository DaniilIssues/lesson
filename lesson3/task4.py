# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 40
MIN_ITEM = -100
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
array_count = []
max_count = 0
index = 0
max_index = []

for i in array:
    count_num = 0
    for q in range(len(array)):
        if i == array[q]:
            count_num += 1
    array_count.append(count_num)

for q in array_count:
    if q > max_count:
        max_count = q
        max_index.append(index)
    index += 1

print(f'Чаще всего встречается {len(max_index)} числа:')
for i in max_index:
    print(array[i])
