# 3.Создайте список из случайных чисел.
# Найдите максимальное количество его одинаковых элементов.

import random
listt = []
count = int(input('Enter the number of items: '))
for i in range(count):
    number = random.randint(1,10)
    listt.append(number)
print(listt)

dict = {}
max = 0
# listt = [1, 2, 3, 2, 1, 2, 3, 4, 5, 4, 3, 6, 5, 4, 6, 7, 6, 5, 4, 3]
for i in set(listt):
    count = 0
    for j in listt:
        if i == j:
            count+=1
    dict[i] = count
print(dict)
for i in dict:
    if dict[i] > max:
        max = dict[i]
for k, v in dict.items():
    if v == max:
        print(k, v)


    


