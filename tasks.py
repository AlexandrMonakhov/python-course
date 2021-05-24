# Задание №1
first_number = int(input("Введите первое число:")) ** 2
second_number = int(input("Введите второе число:")) ** 2
sum = first_number + second_number

print("Сумма квадратов чисел:", sum)

# Задание №2
first_number = int(input("Введите первое число:"))
second_number = int(input("Введите второе число:"))

print(f'{first_number} умноженное на {second_number} равно {first_number * second_number}')
print(f'{first_number} деленное на {second_number} равно {float(first_number / second_number)}')
print(f'{first_number} нацело деленное на {second_number} равно {first_number // second_number}')
print(f'Остаток от деления {first_number} на {second_number} равно {first_number % second_number}')
print(f'{first_number} в степени {second_number} равно {first_number ** second_number}')

# Задание №3
integer_number = abs(int(input("Введите одно целое трехзначное число: ")))
first_number = integer_number // 100
second_number = integer_number % 100 // 10
third_number = integer_number % 10

print(f'Сумма цифр {integer_number} равна {first_number + second_number + third_number}')
print(f'Произведение цифр {integer_number} равна {first_number * second_number * third_number}')

# Задание №4
rubles = int(input("Введите кол-во рублей: "))
kopecks = int(input("Введите кол-во копеек: "))
balls = int(input("Введите кол-во мячей: "))
total_kopecks = (rubles * balls * 100) + (kopecks * balls)
kops = total_kopecks % 100
rubs = (total_kopecks - kops) / 100

print(f'За {balls} мяча нужно заплатить {int(rubs)} рублей {kops} копеек')

# Задание №5
time = int(input("Введите время в секундах: "))
hours = time // 3600
minutes = time % 3600 // 60
seconds = time % 60

print(f'{time} секунд - это {hours} часа {minutes} минут {seconds} сек')

# Задание №6
number = int(input("Введите число и мы найдем максимальное число: "))
first_number = number // 1000
second_number = number % 1000 // 100
third_number = number % 100 // 10
fourth_number = number % 10

print(f'У числа {number} максимальная цифра равна {max(first_number, second_number, third_number, fourth_number)}')

# Задание №7
number = int(input("Введите число: "))
pre_pre_last_number = number % 1000 // 100
pre_last_number = number % 100 // 10
last_number = number % 10

print(f'У числа {number} сумма последних трех цифр равна {pre_pre_last_number + pre_last_number + last_number}')

