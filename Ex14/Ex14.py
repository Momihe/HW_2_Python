# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

a = int(input('Введите предел для максимально числа степени двойки: '))
k = 0
while 2**k <= a: 
    print(f'{k}-я степень числа 2 равна {2**k}')
    k += 1
  