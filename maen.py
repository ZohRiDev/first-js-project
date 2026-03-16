
secret_number1 = 7 
fer2 = 0
while True:
    gerne = int(input('Введите число: '))
    fer2 = fer2 + 1
    if gerne < secret_number1:
        print('Мало мыслишь!')
    elif gerne > secret_number1:
        print('Убавь темп , дружок.')
    else:
        print(f'Крассавчик!Ты отгадал число за {fer2} попыток.')
        break
