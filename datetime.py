import datetime as dt


DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь'
}

UTC_OFFSET = {
    'Санкт-Петербург': 3,
    'Москва': 3,
    'Самара': 4,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Пермь': 5,
    'Воронеж': 3,
    'Волгоград': 4,
    'Краснодар': 3,
    'Калининград': 2
}


def what_time(friend):
    current_time = dt.datetime.utcnow() # напишите код тела функции
    city_time = DATABASE[friend]
    print(city_time)
    now_time = dt.timedelta(hours = UTC_OFFSET[city_time])# пусть она вернет время у друга из аргумента friend
    required_time = current_time + now_time
    return reqired_time


print(what_time('Алина'))
