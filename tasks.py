# # Задание №1
# for i in range(25):
#     print('Hello, GloAcademy!')

# # Задание №2
# number = int(input('Введите число:'))
# for i in range(number + 1):
#     print(f'Квадрат числа {i} равен {i ** 2}')

# # Задание №3
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
#
# for i in range(min(a, b), max(a, b) + 1):
#     print(i)

# # Задание №4
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
#
# for i in range(min(a, b), max(a, b) + 1):
#     if i % 2 == 0:
#         print(i)

# # Задание №5
# number = int(input('Введите число: '))
#
# for i in range(1, 11):
#     print(f'{number} x {i} = {number * i}')

# Задание №6
# print(f'Сумма равна {sum([i for i in range(int(input("Введите число: ")) + 1) if i % 10 in [1, 3, 7]])}')

# Задание №7
number = int(input('Введите число: '))
total = 1

for i in range(number + 1):
    if i % 10 in [2, 9]:
        total *= i

if total == 1:
    print(0)
else:
    print(total)

# Задание №8
num_min = int(input("Введите минимальное число: "))
num_max = int(input("Введите максимальное число: "))
num = int(input("Введите кол-во цифр для ввода далее: "))
if num >= 2:
    for i in range(1, num + 1):
        print("____________________________________")
        number = int(input())
        if number < num_min:
            num_min = number
        if number > num_max:
            num_max = number

    print(f"Минимум равен {num_min}")
    print(f"Максимум равен {num_max}")

# Заданеие №9
flag = 0

num = int(input("Введите кол-во цифр для ввода далее: "))

for i in range(1, num + 1):
    print("____________________________________")
    num = int(input())
    if num % 10 != 2:
        flag = 1
if flag == 1:
    print("YES")
else:
    print("NO")

# Задание №10
flag = 0
num = int(input("Введите кол-во цифр для ввода далее: "))
for i in range(1, num + 1):
    print("____________________________________")
    num = int(input())
    if num % 10 != 2:
        flag += 1
if flag == num:
    print("YES")
else:
    print("NO")

