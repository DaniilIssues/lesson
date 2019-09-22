# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки
# и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

matrix = []

for i in range(4):
    sum_q = 0
    row = []
    for q in range(5):
        if q < 4:
            digit = int(input())
            row.append(digit)
            sum_q += digit
        else:
            row.append(sum_q)
    matrix.append(row)

for i in matrix:
    for q in i:
        print(q, end="\t")
    print()
