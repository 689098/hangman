import random

number = random.randint(0, 101)
num_guess = 0
counter = 0

print('Добро пожаловать в игру "Угадай число"!\nНужно вводить числа от 1 до 100, чтобы угадать загаданное компьютером число.\nПоехали!')

while number != num_guess:
    num_guess = int(input('Введите свою догадку: '))
    n = int(num_guess)
    if n > number:
        print('Ваше число больше загаданного!')
    if n < number:
        print('Ваше число меньше загаданного!')
    if n == number:
        print('Вы угадали!')
    counter += 1

print('Поздравляем! Вы угадали число с {} попыток!'.format(counter))

input()
