# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли 
# этот день выходным.
x = int(input("Введите число: "))
if x > 0 and x < 6:
    print('да')
elif x == 6 or x == 7:
    print('нет')
else:
    print('неверное значение')

# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z (расшифровка этого выражения 
# not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) для всех значений предикат.
x = int(input('Введите число x '))
y = int(input('Введите число y '))
z = int(input('Введите число z '))
for x in range (2):
        for y in range (2):
            for z in range (2):
                print(not (x or y or z) == (not x and not y and not z))
                print (x, y, z)

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт 
# номер четверти плоскости, в которой находится эта точка .
x = int(input('Введите число x '))
y = int(input('Введите число y '))
if x > 0 and y > 0:
    print('1-я четверть')
elif x < 0 and y > 0:
    print('2-я четверть')
elif x < 0 and y < 0:
    print('3-я четверть')
elif x > 0 and y < 0:
    print('4-я четверть')
else:
    print('точка лежит на координатной плоскости')

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в 
# этой четверти (x и y).
n = int(input('Введите номер четверти: '))
if n == 1:
    print('x > 0 and y > 0')
elif n == 2:
    print('x < 0 and y > 0')
elif n == 3:
    print('x < 0 and y < 0')
elif n == 4:
    print('x > 0 and y < 0')
else:
    print('неверное значение четверти')

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними 
# в 2D пространстве.
ax, ay = map(float, input('Введите координаты 1-й точки: ').split())
bx, by = map(float, input('Введите координаты 2-й точки: ').split())
 
print(round(((bx - ax)**2 + (by - ay)**2)**(1 / 2), 3))