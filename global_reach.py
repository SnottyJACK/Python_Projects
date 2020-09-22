# Доступ отовсюду
# Демонстрирует работу с глобальными переменными
def read_global():
    print("В области видимости функции read_global() значение value равно", value)
def shadow_global():
    print("В области видимости функции shadow_global() значение value равно", value)
def change_global():
    global value
    value = -10
