#Задача 14: Требуется вывести все целые степени двойки (т.е. числавида 2k), не превосходящие числа N.
#10 -> 1 2 4 8

N = int(input('Введите число N: '))
res = 1
while 2** res <= N:
    res += 1
    print (2**(res-1))

    
