from math import ceil
# Задание №1
num = int(input('Введите число: '))
count = 0
while num % 2 == 0:
    num = num // 2
    count += 1
print(f'Число {num} делится нацело {count} раз')

# Задание №2
num = int(input('Введите число: '))
total = 0
while num != 0:
    last_digit = num % 10
    if last_digit == 5:
        total += 1

    num = num // 10

print(total)

# Задание №3
num = int(input('Введите число: '))
tmp_num = num
total = 0
while tmp_num != 0:
    total += tmp_num % 10
    tmp_num = tmp_num // 10

    if num % total == 0:
        print("YES")
    else:
        print("NO")

# Задание №4
num = int(input('Введите число: '))
max = 1
min = 1

while num >= 10:
    last_digit = num % 10
    num = num // 10

    if last_digit > max:
        max = last_digit
    if last_digit < min:
        min = last_digit

print(f"Максимальная цифра равна {max}")
print(f"Минимальная цифра равна {min}")

# Задание №5
num = int(input('Введите число: '))
positive = 0
negative = 0

while num != 0:
    num = int(input())
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1

print(f'Произведение кол-ва положительных на отрицательные {positive * negative}')

# Задание №6
num = int(input('Введите число: '))
sum = 0
count = 0

while num != 0:
    num = int(input('Введите число: '))
    count += 1
    sum += num

print(f'Среднее арифметическое равно: {ceil(sum / count)}')
