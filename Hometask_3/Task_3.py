# # *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква
# # имеет определенную ценность. В случае с английским
# # алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# # D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка;
# # K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# # А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# # Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка;
# # Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# # Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# # Будем считать, что на вход подается только одно слово,
# # которое содержит либо только английские, либо только русские буквы.
# # *Пример:*
# # ноутбук
# #     12

# word = list(input('Enter the word: '))
# e_one = ['a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r']
# e_two = ['d', 'g']
# e_three = ['b', 'c', 'm', 'p']
# e_four = ['f', 'h', 'v', 'w', 'y']
# e_five = ['k']
# e_eight = ['j', 'x']
# e_ten = ['q', 'z']
# r_one = ['а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т']
# r_two = ['д', 'к', 'л', 'м', 'п', 'у']
# r_three = ['б', 'г', 'ё', 'ь', 'я']
# r_four = ['й', 'ы']
# r_five = ['ж', 'з', 'х', 'ц', 'ч']
# r_eight = ['ш', 'э', 'ю']
# r_ten = ['ф', 'щ', 'ъ']
# count = 0
# for i in word:
#     if i in e_one or i in r_one:
#         count = count + 1
#     elif i in e_two or i in r_two:
#         count = count + 2
#     elif i in e_three or i in r_three:
#         count = count + 3
#     elif i in e_four or i in r_four:
#         count = count + 4
#     elif i in e_five or i in r_five:
#         count = count + 5
#     elif i in e_eight or i in r_eight:
#         count = count + 8
#     elif i in e_ten or i in r_ten:
#         count = count + 10
#     else:
#         print('You have spelled the word wrong')
# print(count)

# решение с семинара
text = input('Enter the word: ')
dictionary = {'a': '1', 'e': '1', 'i': '1', 'o': '1', 'u': '1', 'l': '1', 'n': '1', 's': '1', 't': '1', 'r': '1',
              'а': '1', 'в': '1', 'е': '1', 'и': '1', 'н': '1', 'о': '1', 'р': '1', 'с': '1', 'т': '1',
              'd': '2', 'g': '2', 'д': '2', 'к': '2', 'л': '2', 'м': '2', 'п': '2', 'у': '2', 
              'b': '3', 'c': '3', 'm': '3', 'p': '3','б': '3', 'г': '3', 'ё': '3', 'ь': '3', 'я': '3',
              'f': '4', 'h': '4', 'v': '4', 'w': '4', 'y': '4', 'й': '4', 'ы': '4',
              'k': '5', 'ж': '5', 'з': '5', 'х': '5', 'ц': '5', 'ч': '5',
              'j': '8', 'x': '8', 'ш': '8', 'э': '8', 'ю': '8',
              'q': '10', 'z': '10', 'ф': '10', 'щ': '10', 'ъ': '10'}
sum = 0
for letter in text:
    sum = sum + int(dictionary[letter.lower()])
print(sum)

# можно в значениях сразу писать числа, чтобы не приводить потом к числу