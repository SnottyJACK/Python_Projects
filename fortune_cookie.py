# Печенье с предсказанием
#
# Author: Satonin Vladimir
# 25.02.2020
#
# Программа, которая выбирает случайное число от 1 до 5 и на основании
# этого выдает одно из предсказаний

import random

count = random.randint(1, 5)
if count == 1:
    print("Сегодня Вам благоволит удача !")
elif count == 2:
    print("Любая задача за которую Вы возметесь будет легко выполнена в этот день")
elif count == 3:
    print("Запаситесь терпением, сегодняшний день будет полон работы")
elif count == 4:
    print("Вы рождены под Счастливой звездой ))")
elif count == 5:
    print("Не переусердствуйте, умейте расслабляться")
