#Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
#массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N
#чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива
#Ввод: Вывод:
#7                                              3 3 2 12
#3 1 3 4 2 4 12
#6
#4 15 43 1 15 1 (каждое число вводится с новой строки)

'''def lst_diff2(list_1: list, list_2: list):
    return [i for i in list_1 if i not in list_2]'''

'''def numbers(x):
    lst_1 = []
    for _ in range(x):
        lst_1.append(int(input('Введите элемент массива: ')))
    return lst_1


def diff_lst(lst_1, lst_2):
    lst_3 = []
    for i in lst_1:
        if i not in lst_2:
            lst_3.append(i)
    return lst_3
            

n = int(input('Введите количество элементов первого массива: '))
lst_n = numbers(n)
print(lst_n)
m = int(input('Введите количество элементов второго массива: '))
lst_m = numbers(m)
print(lst_m)

print(diff_lst(lst_n, lst_m))'''


#Задача №41. Решение в группах Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, у которых два соседних и, при
#этом, оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива. Массив
#состоит из целых чисел.
#Ввод:                         Ввод:
#5                                  5
#1 2 3 4 5                          1 5 1 5 1
#Вывод:                         Вывод:
#0                                   2                           (каждое число вводится с новой строки)
 
'''def numbers(x):
    lst_1 = []
    for _ in range(x):
        lst_1.append(int(input('Введите элемент массива: ')))
    return lst_1

def search_lst(lst_1):
    count = 0
    for i in range(1, len(lst_1) - 1):
        if lst_1[i - 1] < lst_1[i] > lst_1[i + 1]:
            count += 1
    return count

n = int(input('Введите количество элементов первого массива: '))
lst_n = numbers(n)
print(lst_n)
print(search_lst(lst_n))'''

#Задача №43. Решение в группах Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые
#два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список чисел. Все числа списка находятся на разных строках.
#Ввод:                         Вывод:
#1 2 3 2 3                              2

'''def count_pairs(inp_lst: list):
    return sum([inp_lst.count(i) // 2 for i in set(inp_lst)])'''

#Задача №45. Решение в группах Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и
#наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа
#получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести все пары дружественных чисел, каждое из которых не
#превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую
#пару не дает).
#Ввод: Вывод:
#300 220 284

def sum_divisors(num):
    summ = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            # print(f'{i = }')
            summ += i
    return summ


def friends_num(number):
    for i in range(1, number):
        j = sum_divisors(i)
        if i < j <= number and i == sum_divisors(j):
            print(i, j)