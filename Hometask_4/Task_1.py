# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах. 
# Пользователь вводит 2 числа. 
# n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

slist_1 = []
slist_2 = []
count_1 = int(input('Enter the first list number of elements: '))
count_2 = int(input('Enter the second list number of elements: '))
for i in range(count_1):
    number = int(input('Enter the numbers for the first list: '))
    slist_1.append(number)
slist_1 = set(slist_1)
print(slist_1)

for i in range(count_2):
    number = int(input('Enter the numbers for the second list: '))
    slist_2.append(number)
slist_2 = set(slist_2)
print(slist_2)

res_list = list(slist_1.intersection(slist_2))
res_list.sort()
print(res_list)


