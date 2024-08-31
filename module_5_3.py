class House:
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors
    def __str__(self):
        return f'Название {self.name}, количество этажей {self.numbers_of_floors}'
    def __len__(self):
        return self.numbers_of_floors

    def __eq__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors == other.numbers_of_floors

    def __lt__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors < other.numbers_of_floors

    def __le__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors <= other.numbers_of_floors

    def __gt__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors > other.numbers_of_floors

    def __ge__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors >= other.numbers_of_floors

    def __ne__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors != other.numbers_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.numbers_of_floors + value)
        return self.numbers_of_floors

    def __radd__(self, value):
        if isinstance(value, int):
            return House(self.name, self.numbers_of_floors + value)
        return self.numbers_of_floors

    def __iadd__(self, value):
        if isinstance(value, int):
            return House(self.name, self.numbers_of_floors + value)
        return self.numbers_of_floors


    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.numbers_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor):
                print(i)
            print(f'Вы приехали на {new_floor} этаж')


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
