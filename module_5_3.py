# Перегрузка операторов.
# Задача "Нужно больше этажей"

class House:
    wrong_other = 'Данная операция не предусмотрена!'
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

    def my_op(self,house_obj, ops):
        self_nof = self.number_of_floors

        if isinstance(house_obj, House):
            n_of_f = house_obj.number_of_floors
        elif isinstance(house_obj, int):
            n_of_f= house_obj
        else:
            return self.wrong_other

        match ops:
            case '__eq__':
                return self_nof == n_of_f
            case '__lt__':
                return self_nof < n_of_f
            case '__le__':
                return self_nof <= n_of_f
            case '__gt__':
                return self_nof > n_of_f
            case '__ge__':
                return self_nof >= n_of_f
            case '__ne__':
                return self_nof != n_of_f
            case '__add__', '__radd__':
                return self_nof + n_of_f
            case '__iadd__':
                self_nof += n_of_f
                return self_nof
            case '__mul__':
                return self_nof * n_of_f
            case '__imul__':
                self_nof *= n_of_f
                return self_nof
            case '__sub__':
                return self_nof - n_of_f
            case '__isub__':
                self_nof -= n_of_f
                return self_nof
            case '__floordiv__':
                return self_nof // n_of_f
            case '__mod__':
                return self_nof % n_of_f
            case _:
                return self.wrong_other


    def __eq__(self, other):
        return self.my_op(other, '__eq__')


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__
