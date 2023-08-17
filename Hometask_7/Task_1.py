# # Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# # разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# # стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# # гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# # слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# # от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# # напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# # в порядке
# # Ввод: 
# # пара-ра-рам рам-пам-папам па-ра-па-дам 
# # Вывод:
# # Парам пам-пам

# def syll(x):
#     vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'э', 'ю', 'я'] # лучше множество, искать быстрее
#     rythm = []
#     for i in x:
#         phrase = i
#         count = 0
#         for j in phrase:
#             if j in vowels:
#                 count += 1
#         rythm.append(count)
#     return set(rythm)


# song = list(input(). split())
# if len(syll(song)) == 1:
#     print('Парам пам-пам')
# else:
#     print('Пам парам')

# # ---------из семинара---------
# def rythm(strr):
# #   vowels = {'а', 'е', 'ё', 'и', 'о', 'у', 'э', 'ю', 'я'}
#     word_list = strr.split()
#     res_set = set(map(lambda word: word.count('а') + word.count('е') + word.count('ё') + word.count('и') +word.count('о') + word.count('у') + word.count('э') + word.count('ю') + word.count('я'), word_list))
#     if len(res_set) == 1:
#         return "There is rythm"
#     return "There isn't rythm"

# strr = input()
# print(rythm(strr))

#  -------------   еще вариант с фвп -----------
def count_vowels(strr):
    vowels = 'аеёиоуэюя'
    return sum([strr.count(letter) for letter in vowels])

word_list = input().split()
print(("There is not rythm", 'There is rythm')[len(set(map(count_vowels, word_list))) ==1])