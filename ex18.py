#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке
#вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X


from random import randint
size = int(input('Введите размер списка: '))
numbers = tuple(randint(1, size) for _ in range(size))
print(*numbers)
num_X = int(input('Введите искомое число: '))
m = 0
for _ in range(len(set(numbers))):
    for i in set(numbers):
        if i == num_X - m or i == num_X + m:
            print(i)
            m += 1
    