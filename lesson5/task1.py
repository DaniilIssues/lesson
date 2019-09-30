# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import defaultdict

companies = defaultdict(list)
name = 0
average = {}
count_company = int(input('Введите количество предприятий: '))

for i in range(count_company):
    for q in range(5):
        if q == 0:
            name = input('Введите название компании: ')
        else:
            companies[name].append(int(input(f'Введите прибыль за {q} квартал: ')))
    average[name] = sum(companies[name])/4

total_average = sum(average.values())/len(average)
print(f'Средняя прибыль всех предприятий = {total_average}')

for k, v in average.items():
    if v > total_average:
        print(f'Прибыль "{k}" выше среднего.')
    elif v < total_average:
        print(f'Прибыль "{k}" ниже среднего.')
    else:
        print(f'Прибыль "{k}" равна среднему.')

