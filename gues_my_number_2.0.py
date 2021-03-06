# Отгадай число
#
# Author: Satonin Vladimir
# 26.02.2020
#
# Компьютер выбирает случайное число в диапазоне от 1 до 100
# Игрок пытается отгадать это число, и компьютер говорит,
# предложение больше/меньше, чем загаданное число,
# или попало в точку
import random

print("\tДобро пожаловать в игру \"Отгадай число\"!")
print("\nЯ загадал натуральное число из диапазона от 1 до 100.")
print("Постарайтесь отгадать его за 10 попыток.\n")
# Начальные значения
the_number = random.randint(1, 100)
guess = int(input("Ваше предположение: "))
tries = 1

# Цикл отгадывания

while tries < 10:
    if guess == the_number:
        print("Вам удалось отгадать число! Это в самом деле", the_number)
        print("Вы затратили на отгадывание всего лишь", tries, "попыток!\n")
    elif guess > the_number:
        print("Меньше...")
    else:
        print("Больше...")
    guess = int(input("Ваше предположение: "))
    tries += 1
print("\n\n\tВам непомешало бы изучить сортировки".upper())


input("\n\nНажмите Enter, чтобы выйти")
