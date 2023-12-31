# # 1) RLE-сжатие – один из самых простых методов сжатия строки, основанный на сокращении подстрок, 
# # состоящих из одинаковых символов. Сжатие осуществляется следующим образом:
# # Строка разбивается на минимальное количество подстрок, состоящих из одинаковых символов. 
# # Например, abbcaaa превращается в строки a, bb, c, aaa.
# # Каждая из полученных строк превращается в строку, состоящую из числа и буквы. 
# # Числом является количество повторений символа в этой строке, буква берётся из 
# # первого символа обрабатываемой строки. Число не добавляется, если количество символов 
# # в строке равно единице. Из предыдущего массива строк мы получаем a, 2b, c, 3a.
# # Затем полученные строки конкатенируются в исходном порядке. 
# # В рассмотренном примере в итоге получим a2bc3a.
# # Вводится строка, нужно сжать ее по алгоритму, описанному выше.

# line = input('Enter the line: ')
# listt = []
# temp = line[0]
# i = 1
# while i < len(line): #
#     if line[i-1] != line[i]: #
#         listt.append(temp) #
#         temp = line[i] #b
#     if line[i-1] == line[i]:
#         temp = temp + line [i]
#     i +=1
# if temp:
#     listt.append(temp)
# print(listt)

# res_str = ''
# for strr in listt:
#     if len(strr) == 1:
#         res_str = res_str + strr[0]
#     else:
#         res_str = res_str + str((len(strr))) + strr[0]
# print(res_str)

# из семинара решение
stroka = input('Enter the line: ')
res = ''
prev = ''
count = 0
if len(stroka) <= 1:
    res = stroka
else:
    for letter in stroka:
        if letter != prev:
            if prev:
                res += str(count) + prev
            count = 1
            prev = letter
        else:
            count += 1
    else:
        res += str(count) + prev
print(res)
