m = int(input('Минуты: '))
m = m % 3600
print(f'{m // 60:02d}:{m % 60:02d}')