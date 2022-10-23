# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

def Find_miltipliers (num, count, list):
    while count < num+1:
        if num % count != 0:
            count += 1
        elif num % count == 0:
            list.append(count)
            count += 1
    return list
num = int(input('Введите натуральное число: '))
print(f'Простые множители числа {num}: {Find_miltipliers(num, 1, [])}')

