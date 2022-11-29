# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]

lst = [2, 3, 4, 5, 6]
lst1 = [2, 3, 5, 6]
lst2 = [2, 3, 4, 5, 6, 7]
lst3 = [2, 3, 4, 5, 6, 7, 8]

def f(lst):
    l=[]
    if len(lst) % 2 == 0:
        for i in range(len(lst)//2):
            pr_ = lst[i] * lst[2*len(lst)//2-i-1]
            l.append(pr_)
    else:
        for i in range(len(lst)//2+1):
            pr_ = lst[i] * lst[2*len(lst)//2-i-1]
            l.append(pr_)
    return l
l=f(lst)
l1=f(lst1)
l2=f(lst2)
l3=f(lst3)

print(l)
print(l1)
print(l2)
print(l3)
