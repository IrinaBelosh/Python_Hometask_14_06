# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

s = int(input("Enter the number of paper cranes made: "))
x = int(s/6)
if s % 6 == 0:
    print(f"Pete made {x}, Serge made {x}, Kate made {4*x}")
else:
    print("The number is not splittable")




