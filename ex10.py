#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число
#монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
#5 -> 1 0 1 1 0
#2
from random import randint
k = 5
list_coins = []
for i in range (k):
    list_coins.append(randint(0,1))
print(list_coins)
zero = list_coins.count(0)
if len(list_coins) - zero < zero:
    print(len(list_coins - zero))
else:
    print(zero)



