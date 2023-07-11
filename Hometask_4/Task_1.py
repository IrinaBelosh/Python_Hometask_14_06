# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах. 
# Пользователь вводит 2 числа. 
# n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# вариант 1
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

# вариант 2
list_1 = [int(x) for x in input('Enter numbers with gaps: ').split()]
list_1 = set(list_1)
print(list_1)
list_2 = [int(y) for y in input('Enter numbers with gaps: ').split()]
list_2 = set(list_2)
print(list_2)
inters = list(list_1 & list_2)
inters.sort()
print(inters)