articles_list = [
    [1, "Айви Яптанго", 2020, "Самые шикарные парочки знаменитостей 2019 года", ["красота", "гороскопы"]],
    [2, "Лео Месси", 2014, "Un Abrazo a Todos", ["лайфстайл", "недвижимость"]],
    [3, "Гэри Паска", 2016, "Продаётся дом в Южной Флориде за $2,695", ["недвижимость", "коучинг", "howto"]],
    [4, "Роби Тобинсон", 1967, "7 лет я применял этот трюк и назад пути нет", ["лайфхак", "коучинг", "howto"]],
    [5, "Металлий Вутко", 2017, "Let Me Speak From My Heart", ["футбол", "допинг"]],
    [6, "Роби Тобинсон", 1977, "Беспроигрышная древнеримская техника обольщения", ["отношения", "история", "howto"]],
    [7, "Роби Тобинсон", 2022, "3 способа установить девайс от храпа", ["здоровье", "коучинг", "howto"]],
    [8, "Роби Тобинсон", 1975, "Интимная проблема, которой втайне озабочены все ваши друзья", ["отношения", "здоровье", "howto"]],
    [9, "Elina Shake", 2008, "Представления, основанные на классах", ["python", "howto", "лайфхак"]],
    [10, "Бен Франклин", 1753, "Электрические стодолларовые купюры", ["фондовая биржа", "рынки", "электричество"]],
    [11, "Роби Тобинсон", 2012, "5 забавных Django Apps, о которых говорят все", ["django", "IT", "howto"]],
    [12, "Металлий Вутко", 2017, "No Problems, No Criminality", ["допинг", "недвижимость"]],
    [13, "Роби Тобинсон", 1987, "7 способов до смерти напугать своего босса в пятницу 13-го", ["работа", "мистика", "howto"]],
    [14, "Твентин Карантино", 2007, "Четыре сервера", ["кино", "django", "мистика"]],
]



def add_tag(author):
    author_articles = []
    for article in articles_list:
        if article[1] == author:
            author_articles.append(article)



    return  print(author_articles, end='')


def main(author):
    return add_tag(author)

main('Роби Тобинсон')