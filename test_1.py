while True:
    comand = input('Введите операцию: ')
    if comand in '+-*/':
        break
    print('Ошибка, такой операции не существует. Попробуйте еще раз!')

count = 1
number = int(input(f'Введите число {count}: '))
result_str = str(number)
result = number
while number != 0:
    count += 1
    number = int(input(f'Введите число {count}'))

    if number != 0:
        if comand == '+':
            result += number
        elif comand == '-':
            result -= number
        elif comand == '*':
            result *= number
        elif comand == '/':
            result /= number
    result_str += ' ' + comand + ' ' + str(number)

print(result_str + ' = ' + str(result))

while True:
    comand = input('Введите операцию: ')
    if comand in '+-*/':
        break
    print('Ошибка, такой операции не существует. Попробуйте еще раз!')

