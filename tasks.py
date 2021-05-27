# Задание №1
number = input('Введите число: ')
print(f'Длина введенного числа равна {len(number)}')

# Задание №2
post = input('Введите текст: ')

if 'Glo Academy' in post:
    print('YES')
else:
    print('NO')

# Задание №3
post_1 = input('Введите текст статьи: ')
post_2 = input('Введите текст статьи: ')
post_3 = input('Введите текст статьи: ')

print(max(post_1, post_2, post_3))

# Задание №4
team = input('Введите название команды: ')
print(team * 5)

# Задание №5
email = input('Введите ваш Email: ')

if '@' and '.' in email:
    print('Корректный')
else:
    print('Некорректный')
