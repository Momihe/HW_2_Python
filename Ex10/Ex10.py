# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно 
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

import random 
a = int(input('Введите количество монеток: '))
mass = [random.randint(0,1) for i in range(a)]
print('Положение монеток. 1 - орел, 0 - решка')
print(*mass)
eagle = 0
zero = 0
for i in mass:
    if i == 0: zero += 1
    else: eagle += 1   
print (f'Количество орлов: {eagle}.\nКоличество решек: {zero}.')
if eagle == 0 or zero == 0: print('Ничего крутить не надо.') 
elif eagle > zero: print('Рациональнее переворачивать решки.')
elif eagle < zero: print('Рациональнее переворачивать орлы.')  
else: print('Переворачивай что хочешь.')