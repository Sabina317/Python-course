while True:
    day_x = 1
    beginning = float(input('Введите результат первого дня пробежки в км - '))
    end = float(input('Введите желаемый результат пробежки в км - '))
    if beginning <= 0 or end <= 0 or end < beginning:
        print('Введите положительное возрастающее значение')
    else:
        while beginning < end:
            beginning *= 1.1
            day_x += 1

        print(f'Через {day_x} дней будет достигнут результат')
        break
