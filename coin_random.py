# Подбрасывание монетки
#
# Author: Satonin Vladimir
# 25.02.2020
#
# Программа подбрасывает условную монету 100 раз и сообщает, сколько раз
# выпал орел, а сколько решка

import random
eagle = 0
tails = 0
count = 0
while count != 100:
    coin = random.randint(1, 2)
    if coin == 1:
        eagle += 1
    else:
        tails += 1
    count += 1
print("Орел выпал: ", eagle, "раз")
print("Решка выпала: ", tails, "раз")
