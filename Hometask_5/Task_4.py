# 4.Создайте список из случайных чисел. Найдите второй максимум.
# a = [1, 2, 3] # Первый максимум == 3, второй == 2

import random
some_list = []
count = int(input('Enter the number of items: '))
for i in range(count):
    number = random.randint(1,10)
    some_list.append(number)
print(some_list)

max1 = max(some_list)
max2 = 0
for i in range(len(some_list)):
    if max2 <= some_list[i] < max1:
        max2 = some_list[i]
print(max2)

