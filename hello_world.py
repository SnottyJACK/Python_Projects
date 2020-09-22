name = input('Введите ваше имя: ')
try:
    s = input("Введите данные: ")
    print(s)
except EOFError:
    print("Обработали исключение EOFError")
print("Привет,", name)
input("Нажмите <Enter> для закрытия окна")
