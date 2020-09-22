def print_shopping_list(dish1, dish2):
    ingredients = set(dish1.keys()).union(set(dish2.keys()))
    print(ingredients)
    for i in ingredients:
        amount = 0
        if i in dish1.keys():
            amount += dish1[i]
        if i in dish2.keys():
            amount += dish2[i]
        print(i, ":", amount)

# подобрав уникальные названия продуктов и сложив значения


pizza = {'мука, кг': 1,
         'помидоры, кг': 1.5,
         'шампиньоны, кг': 1.5,
         'сыр, кг': 0.8,
         'оливковое масло, л': 0.1,
         'дрожжи, г': 50}
salad = {'огурцы, кг': 1,
         'перцы, кг': 1,
         'помидоры, кг': 1.5,
         'оливковое масло, л': 0.1,
         'листья салата, кг': 0.4}

print_shopping_list(pizza, salad)
