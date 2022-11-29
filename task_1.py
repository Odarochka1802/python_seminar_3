# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random
l=[random.randint(0,99) for i in range(random.randint(1,10))]
print(l)
def sum_number(lst,summa=0):
    for i in range(1,len(lst),2):
        summa+=lst[i]
    return summa
s=sum_number(l)
print(s)

    
