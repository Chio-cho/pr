class Dish:
    def __init__(self, name, category, price, weight):
        self.name = name
        self.category = category
        self.price = int(price)
        self.weight = int(weight)

    def __str__(self):
        return f"Dish: {self.name}, Категория: {self.category}, Стоимость: {self.price}, Вес: {self.weight}"
class Menu:
    def __init__(self, f="aaaa.txt"):
        self.menu_dict = self.read(f)
    def __iter__(self):
        return iter(self.menu_dict.values())

    def read(self, f):
        dishes = {}
        with open(f, 'r') as file:
            for line in file:
                name, category, price, weight = line.strip().split(', ')
                price = int(price)
                weight = int(weight)
                dishes[name] = Dish(name, category, price, weight)
        return dishes

