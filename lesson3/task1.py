# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

MIN_ITEM = 2
MAX_ITEM = 99

array = [_ for _ in range(MIN_ITEM, MAX_ITEM + 1)]
array_2 = [_ for _ in range(2, 10)]

for i in array_2:
    n = 0
    for q in array:
        if q % i == 0:
            n += 1
    print(f'{n} чисел кратны {i}.')

