# Задача 32: Определить индексы элементов массива (списка), значения 
# которых принадлежат заданному диапазону (т.е. не меньше заданного 
# минимума и не больше заданного максимума)

# import random
# scope = int(input('Enter the scope of a list: '))
# listt = []
# for i in range(1, scope+1):
#     listt.append(random.randint(1,100))
# print(listt)

import random
scope = int(input('Enter the scope of a list: '))
listt = [random.randint(1,100) for _ in range(1, scope+1)]
print(listt)
maxx = int(input('Enter the max of a spun: '))
minn = int(input('Enter the min of a spun: '))
print(f'The spun is ({minn} : {maxx})')
for i in range(len(listt)):
    if minn < listt[i] < maxx:
        print(i, end= ',')