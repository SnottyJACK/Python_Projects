def print_shopping_list(recipe1, recipe2):# напишите здесь свою функцию
    recipe1 = set(recipe1)
    recipe2 = set(recipe2)
    recipe3 = recipe1.union(recipe2)
    print(', '.join(recipe3))

pizza = ['мука', 'помидоры', 'шампиньоны', 'сыр', 'оливковое масло']
salad = ['огурцы', 'перцы', 'помидоры', 'оливковое масло', 'листья салата']

print_shopping_list(pizza, salad)
