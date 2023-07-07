# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква
# имеет определенную ценность. В случае с английским
# алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка;
# K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово,
# которое содержит либо только английские, либо только русские буквы.
# *Пример:*
# ноутбук
#     12

word = list(input('Enter the word: '))
e_one = ['a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r']
e_two = ['d', 'g']
e_three = ['b', 'c', 'm', 'p']
e_four = ['f', 'h', 'v', 'w', 'y']
e_five = ['k']
e_eight = ['j', 'x']
e_ten = ['q', 'z']
r_one = ['а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т']
r_two = ['д', 'к', 'л', 'м', 'п', 'у']
r_three = ['б', 'г', 'ё', 'ь', 'я']
r_four = ['й', 'ы']
r_five = ['ж', 'з', 'х', 'ц', 'ч']
r_eight = ['ш', 'э', 'ю']
r_ten = ['ф', 'щ', 'ъ']
count = 0
for i in word:
    if i in e_one or i in r_one:
        count = count + 1
    elif i in e_two or i in r_two:
        count = count + 2
    elif i in e_three or i in r_three:
        count = count + 3
    elif i in e_four or i in r_four:
        count = count + 4
    elif i in e_five or i in r_five:
        count = count + 5
    elif i in e_eight or i in r_eight:
        count = count + 8
    elif i in e_ten or i in r_ten:
        count = count + 10
    else:
        print('You have spelled the word wrong')
print(count)
