from math import pi

r = input('Радиус орбиты (млн. км): ')
v = input('Орбитальная скорость (км/с): ')
r = float(r)
v = float(v)

r = r * 1000000

year = 2 * pi * r / v

year = year / (60 * 60 * 24)

print(round(year))
