# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x + 53 = 0

# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x + 53 = 0

def Get_Indexes (text_file):
    _ = 0
    result_list = []
    count = 0
    i = 0
    while i < len(text_file):
        if i == len(text_file)-1:
            return result_list
        if (text_file[i] == '-'):
            if (text_file[i+2] == 'x'):
                _ = i + 2
                if (text_file[_] == 'x') & (text_file[_+2].isdigit()):
                    text_file[i] = text_file[i] + text_file[_]
                    count += 2
                    i = _ + 3
                    break
                elif (text_file[_] == 'x') & (text_file[_+2].isdigit() == False):
                    result_list.append('1')
                    count += 2
                    i = _ + 3
                    break
                else:
                    result_list.append('0')
                    count += 2
                    i = _ + 3
                    break
                
            result_list.append(text_file[i])
            _ = i + 2
            while text_file[_].isdigit():
                result_list[count] = result_list[count] + text_file[_]
                _ += 1
            if (text_file[_] == 'x') & (text_file[_+2].isdigit()):
                result_list.append(text_file[_+ 2])
                count += 2
                i = _ + 3
                continue
            elif (text_file[_] == 'x') & (text_file[_+2].isdigit() == False):
                result_list.append('1')
                count += 2
                i = _ + 3
                continue
            else:
                result_list.append('0')
                count += 2
                i = _ + 3
                continue

        if (text_file[i].isdigit()):
            result_list.append(text_file[i])
            _ = i + 1
            while text_file[_].isdigit():
                result_list[count] = result_list[count] + text_file[_]
                _ += 1
            if (text_file[_] == 'x') & (text_file[_+2].isdigit()):
                result_list.append(text_file[_+ 2])
                count += 2
                i = _ + 3
                continue
            elif (text_file[_] == 'x') & (text_file[_+2].isdigit() == False):
                result_list.append('1')
                count += 2
                i = _ + 3
                continue
            else:
                result_list.append('0')
                count += 2
                i = _ + 3
                continue

        if (text_file[i] == 'x'):
            result_list.append('1')
            _ = i + 2
            if (text_file[i] == 'x') & (text_file[_].isdigit()):
                result_list.append(text_file[i+ 2])
                count += 2
                i = _ + 1
            elif (text_file[i] == 'x') & (text_file[_+2].isdigit() == False):
                result_list.append('1')
                count += 2
                i = _ + 1
            else:
                result_list.append('0')
                count += 2
                i = _ + 1
                continue
        i += 1


data_1 = open('5_1.txt', 'r')
Poly_1 = data_1.readline()
data_1.close()

data_2 = open('5_2.txt', 'r')
Poly_2 = data_2.readline()
data_2.close()

def Find_Sum (list_1, list_2):
    summand_list = []
    for i in range(1, len(list_1), 2):
        for j in range(1, len(list_2), 2):
            if list_1[i] == list_2[j]:
                if list_1[i] == ' ':
                    continue
                if list_1[i] == '0':
                    summand_list.append(str(int(list_1[i-1]) + int(list_2[j-1])))
                    list_1[i] = ' '
                    list_1[i-1] = ' '
                    list_2[j] = ' '
                    list_2[j-1] = ' '
                    break
                if list_1[i] != 0:                    
                    summand_list.append(str((int(list_1[i-1]) + int(list_2[j-1]))) + f'x^{list_1[i]}')
                    list_1[i] = ' '
                    list_1[i-1] = ' '
                    list_2[j] = ' '
                    list_2[j-1] = ' '
                    break

    _ = 0
    while _ in range(len(list_1)):
        if list_1[_] == ' ':
            list_1.remove(' ')
            continue
        _ += 1
    _ = 0
    while _ in range(len(list_2)):
        if list_2[_] == ' ':
            list_2.remove(' ')
            continue
        _ += 1
    result = ''
    count = 0
    while count < len(summand_list):
        tmp = summand_list[count]
        if (tmp[0] != '-') & (count != 0):
            summand_list[count] = '+' + summand_list[count]
        result = result + summand_list[count]
        count += 1
    count = 0
    while count < len(list_1):
        if list_1[count+1] != 0:
            tmp = list_1[count]
            if tmp[count] != '-':
                list_1[count] = '+' + list_1[count]
            result = result + f'{list_1[count]}x^{list_1[count+1]}'
            count += 2
        else:
            tmp = list_1[count]
            if tmp[count] != '-':
                list_1[count] = '+' + list_1[count]
            result = result + str(list_1[count])
            count += 2
    count = 0
    while count < len(list_2):
        if list_2[count+1] != 0:
            tmp = list_2[count]
            if tmp[0] != '-':
                list_2[count] = '+' + list_2[count]
            result = result + f'{list_2[count]}x^{list_2[count+1]}'
            count += 2
        else:
            tmp = list_1[count]
            if tmp[0] != '-':
                list_2[count] = '+' + list_2[count]
            result = result + str(list_2[count])
            count += 2   
    
    return result


result = (Find_Sum(Get_Indexes(Poly_1), Get_Indexes(Poly_2))) + ' = 0'

result_file = open('5_result.txt', 'w+')
result_file.write(result)
result_file.close
