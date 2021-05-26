from math import ceil
# Задание №1
password = input('Введите пароль: ')
confirm_password = input('Введите пароль еще раз: ')

if password == confirm_password:
    print('Все хорошо!')
else:
    print('Пароли не совпадают!')

# Задание №2
number = int(input('Введите число: '))

if number > 0:
    print('Число положительное!')
elif number < 0:
    print('Число отрицательное!')
else:
    print('Ноль!')

# Задание №3
ticket = input('Введите номер билета: ')
s1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
s2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
if s1 == s2:
    print(f'Билет {ticket} счастливый!')
else:
    print(f'Билет {ticket} НЕсчастливый!')

# Задание №4
weight = int(input('Введите вес дыни - целое число от 0 до 100: '))
if 0 <= weight <= 100:
    if weight > 2 and weight % 2 == 0:
        print('YES')
    else:
        print('NO')
else:
    print(f'Дыня не может весить {weight} кг!')

# Задание №5
hw_count = int(input('Введите кол-во домашек: '))
days_count = int(input('Введите кол-во дней на выполнение: '))

print(f'На выполнение домашек у тебя уйдет {ceil(hw_count / days_count)} дней!')

# Задание №6
pocket = int(input('Введите номер кармана: '))

if 0 <= pocket <= 36:
    if pocket == 0:
        print(f"Число {pocket} принадлежит зеленому карману")
    elif pocket % 2 == 0:
        if 19 <= pocket <= 28 or 0 < pocket <= 10:
            print(f"Карман {pocket} четный черный")
        elif 29 <= pocket <= 36 or 11 <= pocket <= 18:
            print(f"Карман {pocket} четный красный")
    elif pocket % 2 != 0:
        if 19 <= pocket <= 28 or 0 < pocket <= 10:
            print(f"Карман {pocket} нечетный красный")
        elif 29 <= pocket <= 36 or 11 <= pocket <= 18:
            print(f"Карман {pocket} нечетный черный")
else:
    print("Ошибка ввода! Ведено число вне диапазона 0 - 36")


