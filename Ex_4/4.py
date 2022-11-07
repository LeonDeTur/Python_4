# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k.
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
# Записываем результат в файл.

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

import random

coef = int((input('Введите натуральную степень k: ')))

if coef is (not int and coef <= 0):
    print('Вы ввели не натуральное число.')
    quit()

coef_list = []

for _ in range(coef):
    coef_list.append(random.randint(-100, 100))

result = f'k={coef} -> '
i = 0
while coef > 0:
    if i == 0:
        result = result + f'{coef_list[i]}x^{coef} '
    elif coef_list[i] == 0:
        continue
    elif coef_list[i] < 0:
        result = result + f'- {coef_list[i]*(-1)}x^{coef} '
    else:
        result = result + f'+ {coef_list[i]}x^{coef} '
    i += 1
    coef -= 1

result = result + '= 0'
print (result)

data = open('4.txt', 'a')
data.write (f'{result}\n')
data.close()