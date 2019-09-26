# n = int(input("Введите число: "))
import cProfile


# Вариант 1 (решето эратосфена)
# def simple_digit(n):
#     l = list(range(2, n))
#     for i in l:
#         for q in l[i:]:
#             if q % i == 0:
#                 l.remove(q)
#     return l

# "task2.simple_digit(50)"
# 100 loops, best of 5: 28.3 usec per loop
# "import task2" "task2.simple_digit(100)"
# 100 loops, best of 5: 87.1 usec per loop
# "task2.simple_digit(200)"
# 100 loops, best of 5: 263 usec per loop
# 33    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects} // 50
# 73    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects} // 100
# 152    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects} // 200


# Вариант 2 (рекурсия)
# def simple_digit2(n, j=2):
#     if n < 2:
#         return False
#     if j == n:
#         return True
#     if n % j == 0:
#         return False
#     return simple_digit2(n, j + 1)
#
#
# def run_simple(n):
#     l = []
#     for i in range(n):
#         if simple_digit2(i):
#             l.append(i)
#     return l

# "import task2" "task2.run_simple(50)"
# 100 loops, best of 5: 144 usec per loop
# "task2.run_simple(100)"
# 100 loops, best of 5: 480 usec per loop
# "task2.run_simple(200)"
# 100 loops, best of 5: 2.03 msec per loop


# 366/50    0.000    0.000    0.000    0.000 task2.py:25(simple_digit2) // 50
#         1    0.000    0.000    0.000    0.000 task2.py:34(run_simple)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        15    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#  1159/100    0.001    0.000    0.001    0.000 task2.py:25(simple_digit2) // 100
#         1    0.000    0.000    0.001    0.001 task2.py:34(run_simple)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#        25    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#  4471/200    0.003    0.000    0.003    0.000 task2.py:25(simple_digit2) // 200
#         1    0.000    0.000    0.003    0.003 task2.py:34(run_simple)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#        46    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
