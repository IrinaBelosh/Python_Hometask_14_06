# Задача 18: Требуется найти в массиве A[1..N] самый близкий
# по величине элемент к заданному числу X. Пользователь в первой
# строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
number = int(input("Enter the number: "))
list = [random.randint(1, number) for i in range(1, number+1)]
print(list)
ix = int(input("Enter the number want the closest ones to: "))
list_max = [i for i in list if 0 < i < ix]
list_min = [i for i in list if ix < i < number+1]
print(f"The closest to {ix} are numbers {max(list_max)} and {min(list_min)}")
