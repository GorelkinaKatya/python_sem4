n = int(input('Введите количество элементов в 1-м списке: '))
m = int(input('Введите количество элементов во 2-м списке: '))

from random import randint
list_1 = [randint(-5, 5) for i in range(0, n)]
list_2 = [randint(-5, 5) for i in range(0, m)]

unic_list = list(set([*list_1, *list_2]))
unic_list.sort()

print(f'1-й список: {list_1}\n2-й список: {list_2}\nИтоговый список: {unic_list}')

