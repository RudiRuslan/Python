# Объявите анонимную функцию(лямбда) для определения вхождения в переданную ей строку фрагмента "plr".
# То есть, функция должна возвращать True, если такой фрагмент присутствует в строке и False в противном случаи.

string = input("Введите строку: ")
result = (lambda x: 'plr' in x)(string)
print(result)

# Найти НОД двух чисел.

import random 
a = random.randint(10, 1000)
b = random.randint(10, 1000)
c = [a, b]
print(c)
while max(a,b) % min(a,b) != 0:
    if a > b:
        a = a % b
    elif a < b:
        b = b % a
print(min(a,b))

# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
data = input("Введите строку: ").split()
count = 0
for i in data:
    for j in "абв":
        if j in i.lower():
            count = count + 1
    if count == 3:
        data.remove(i)
    count = 0
print(*data, sep=' ')