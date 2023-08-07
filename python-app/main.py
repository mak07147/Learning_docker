import calendar
print('Добро пожаловать в SUPER календарь\n')

year = int(input('Пожалуйста введите год: '))
month = int(input('Введите номер любого месяца: '))

print(calendar.month(year, month))

print('Все-го хо-ро-ше-го!')