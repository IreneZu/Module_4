# Атрибуты и методы объекта.
# Задача "Developer - не только разработчик"

class House:
    def __init__(self, name, number_of_floors ):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor=1):
        if 0 < new_floor <= self.number_of_floors:
            print(*(i+1 for i in range(new_floor)), sep = '\n')
        else:
            print("Такого этажа не существует")

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(3)