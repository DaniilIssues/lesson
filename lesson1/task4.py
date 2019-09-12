# писать программу, которая генерирует в указанных пользователем границах:
# ● случайное целое число,
# ● случайное вещественное число,
# ● случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
import random

a, b = input("Введите a: "), input("Введите b: ")

if a.isdigit():
    print(random.randint(int(a), int(b)))
elif a.isalpha():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    print(alpha[random.randint(alpha.find(a), alpha.find(b))])
else:
    print(random.uniform(float(a), float(b)))

