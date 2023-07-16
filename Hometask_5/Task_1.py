# 1) RLE-сжатие – один из самых простых методов сжатия строки, основанный на сокращении подстрок, 
# состоящих из одинаковых символов. Сжатие осуществляется следующим образом:
# Строка разбивается на минимальное количество подстрок, состоящих из одинаковых символов. 
# Например, abbcaaa превращается в строки a, bb, c, aaa.
# Каждая из полученных строк превращается в строку, состоящую из числа и буквы. 
# Числом является количество повторений символа в этой строке, буква берётся из 
# первого символа обрабатываемой строки. Число не добавляется, если количество символов 
# в строке равно единице. Из предыдущего массива строк мы получаем a, 2b, c, 3a.
# Затем полученные строки конкатенируются в исходном порядке. 
# В рассмотренном примере в итоге получим a2bc3a.
# Вводится строка, нужно сжать ее по алгоритму, описанному выше.


line = input('Enter the line: ')
listt = []
temp = ''
i = 0
while i + 1 < len(line):
    if line[i] != line[i + 1]:
        temp = temp+line[i]
        listt.append(temp)
        temp = ''
        i += 1
    if line[i] == line[i+1]:
        temp = temp + line [i]
        i +=1
if line[-1] == line[-2]:
    temp = temp+line[-1]
    listt.append(temp)
else:
    listt.append(line[-1])

print(listt)
temp_list = []
for i in range(len(listt)):
    r = str(listt[i])
    var = r[0]
    if len(r) != 1:
        temp_list.append(len(r))
    temp_list.append(var)
print(''.join(map(str,temp_list)))














#     count = 0
#     for j in line:
#         if i == j:
#             count+=1
#     dict[i] = count
# print(dict)
# for i in dict:
#     if dict[i] > max:
#         max = dict[i]
# for k, v in dict.items():
#     if v == max:
#         print(k, v)






   


    
