# 2.Создайте список из случайных чисел. 
# Найдите номер его последнего локального максимума 
# (локальный максимум — это элемент, который больше любого из своих соседей).

import random
listt = []
count = int(input('Enter the number of items: '))
for i in range(count):
    number = random.randint(1,10)
    listt.append(number)
print(listt)

ind = 0
for i in range(1, len(listt)-1):
    if listt[i] > listt[i-1] and listt[i]> listt[i+1]:
        ind = i
        print(ind, end=', ')

