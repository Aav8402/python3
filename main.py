

# Задача 1. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# num = int(input('Введите размер списка '))
# list = []
# sum = 0
# for i in range(num):
#     list_num = int(input(f'Введите число {i+1} '))
#     list.append(list_num)
#     if i % 2 != 0:
#         sum += list[i]
#
# print(list)
# print(f'Сумма нечетных чисел равна {sum}')



# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:[2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]


num = int(input('Введите размер списка '))
list = []
list2 = []
i = 0
for i in range(num):
    list_num = int(input(f'Введите число {i+1} '))
    list.append(list_num)


if len(list)%2 == 0:
    size = len(list) // 2
import math
size = math.ceil(len(list)/2)
print(size)
list2 = []
for i in range(size):
    list2.append(list[i]*list[-i - 1])
print(list2)
