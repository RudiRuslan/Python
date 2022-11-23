#Напишите программу,которая принимает на вход два числа и проверяет,является ли одно 
#число квадратом другого.
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# if b == a * a:
#     print('да')
# elif b * b == a:
#     print('да')
# else:
#     print('нет')
#Напишите программу, которая будет принимать на вход дробь и показывает первую цифру дробной части.
# def use_input_float_number(msg):    #функция ввода дробного числа
#     while True:
#         try:
#             number = float(input(msg))
#             return number
#         except ValueError:
#             print('Введите дробное число: ')

# num_float = use_input_float_number('Введите дробное число: ')
# print(int(num_float * 10)%10)

#Напишите программу,которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
# def use_input_int_number(msg):   #функция ввода целого числа
#     while True:
#         try:
#             number = int(input(msg))
#             return number
#         except ValueError:
#             print('Введите целое число: ')

# num_check = use_input_int_number('введите целое число: ')
# if (num_check % 5 == 0 and num_check % 10 == 0 or num_check % 15 == 0 ) and num_check % 30 != 0:
#     print(True)
# else:
#     print(False)

