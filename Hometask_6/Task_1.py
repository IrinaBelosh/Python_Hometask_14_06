# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки

a = int(input('Enter the first item: '))
d = int(input('Enter the difference: '))
n = int(input('Enter the number of items: '))
print(f'The first item {a}, the difference {d}, the number of items {n}')
listt = [a + (i-1) * d for i in range(1, n + 1)]
print(listt)