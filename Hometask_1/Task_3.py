# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, 
# вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

number = input("Enter the number of the ticket: ")
if len(number)==6:
    number = int(number)
    a = 0
    b = 0
    while number>1000:
        a = a+number%10
        number = number//10
    while number>0:
        b = b +number%10
        number = number//10
    if a==b:
        print("Lucly number")
    else:
        print("Not lucky")
else:
    print("Number is too short")

# решение через срезы строки
number = input("Enter the number of the ticket: ")
if len(number)==6:
    left = int(number[0]) + int(number[1]) + int(number[2])
    right = int(number[3]) + int(number[4]) + int(number[5])
if left==right:
    print('YES')
else:
    print('NO')

    

    
