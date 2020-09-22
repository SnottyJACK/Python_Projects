score = int(input("Введите стоимость автомобиля в рублях: "))
score_13_percent = int(score * 0.13)
register_10_percent = int(score * 0.10)
agent = 5000
delivery = 2500
all_score = score + score_13_percent + register_10_percent + agent + delivery

print("Общая стоимость автомобиля: ", all_score)
