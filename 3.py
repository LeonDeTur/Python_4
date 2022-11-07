# Задайте последовательность цифр. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

import string


num = '1113384455229'
list = []
for _ in range(len(num)):
    for i in range(len(num)):
        if _ == i:
            continue
        elif num[_] == num[i]:
            tmp = None
            break
        else:
            tmp = (num[_])
    if tmp is not None:
        list.append([tmp])

print (list)
