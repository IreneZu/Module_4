# Различие атрибутов класса и экземпляра
# Задача "История строительства"

class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history += [args[0]]
        return super().__new__(cls)

    def __init__(self, name, number_of_floors ):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

# Автоматический запуск удаления последнего объекта h1