
# Задача 16: Требуется вычислить, сколько раз встречается некоторое 
# число X в массиве A[1..N]. Пользователь в первой строке 
# вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

number = int(input("Enter the number: "))
# list = [i for i in range(1, number+1)]
# print(list)
import random
list = [random.randint(1, number) for i in range(1, number+1)]
print(list)
ix = int(input("Enter the number want: "))
print(list.count(ix))