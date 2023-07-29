bushes_number = int(input('Введите количество кустов: '))

from random import randint
berry_list = [randint(0, 10) for i in range(0, bushes_number)]
print(f'Количество ягод на кустах: {berry_list}')

berry_list.append(berry_list[0])
berry_list.append(berry_list[1])
max_berry_sum = 0
for i in range(len(berry_list) - 2):
    if berry_list[i] + berry_list[i+1] + berry_list[i+2] > max_berry_sum:
        max_berry_sum = berry_list[i] + berry_list[i+1] + berry_list[i+2]
print(f'Максимальное число ягод: {max_berry_sum}')