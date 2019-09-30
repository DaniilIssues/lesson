# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элемент[‘C’, ‘4’, ‘F’]фры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и  соответственно.
# Сумма чисел из примера:                                 [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque


one_ = 'C4F'
two_ = 'A2'
table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


def split_(string):
    list_ = deque()
    for i in string:
        list_.append(table.index(i))
    return list_


def convert(list_):
    list_2 = []
    for i in list_:
        list_2.append(table[int(i)])
    return list_2


def sum_(one, two):
    one = split_(one)
    two = split_(two)
    result = deque()
    n = -1
    m = 0
    if len(one) > len(two):
        max_list = one
        min_list = two
    else:
        max_list = two
        min_list = one
    for i in reversed(max_list):
        try:
            result.appendleft(i + min_list[n])
            if m > 0:
                result[0] += 1
                m = 0
            if result[0] > 15:
                m += 1
                result[0] -= 16
                if max_list.index(i) == -1:
                    result.appendleft(1)
            n -= 1
        except IndexError:
            result.appendleft(i)

    return convert(result)


print(split_(one_), split_(two_), sum_(one_, two_), sep='\n')
