# Вычислить число Пи c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

# !!ВНИМАНИЕ

# !!! не использовать константу math.pi

import math

input = int(input('Введитие точность вычисления числа Pi в количестве знаков после запятой (например, 3) (максимальная точность вычисления 14 знаков): '))

def arctg (num, accuracy):
    result = 0
    _ = 1
    while _ < accuracy+1:
        result = result + ((-1)**(_-1) * num**(2*_-1)) / (2*_-1)
        _ += 1
    
    return result

Pi = str(16*arctg(1/5,input) - 4*arctg(1/239,input))
result = '' 
for _ in range(input+2):
    result = result + Pi[_]

print(f'Число Pi с точностью до {input}-го знака после запятой: {result}')