class check():
    def __init__(self):
        self.n = []
    def add(self, a):
        return self.n.append(a)
    def remove(self, b):
        self.n.remove(b)
    def dis(self):
        return (self.n)

obj = check()

choice = 1
while choice != 0:
    print("0. Exit")
    print("1. Add")
    print("2. Delete")
    print("3. Display")
    choice = int(input("Выберите одно из этих значений: "))
    if choice == 1:
        n = int(input("Введите число для добавления в список: "))
        obj.add(n)
    elif choice == 2:
        n = int(input("Введите число, которое хотите удалить: "))
        obj.remove(n)
    elif choice == 3:
        print("Список: ", obj.dis())
    elif choice == 0:
        print("Выходим!")
    else:
        print("Неверный выбор!!")
print()
