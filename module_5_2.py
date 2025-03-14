# Специальные методы классов.
# Задача "Магические здания"

class House:
    def __init__(self, name, number_of_floors ):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor=1):
        if 0 < new_floor <= self.number_of_floors:
            print(*(i+1 for i in range(new_floor)), sep = '\n')
        else:
            print("Такого этажа не существует")
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
# __str__
print(h1)
print(h2)
# __len__
print(len(h1))
print(len(h2))