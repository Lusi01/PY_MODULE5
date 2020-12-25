# базовый класс Food
class Food:

    def __init__(self, title):
        if Food.check_title(title):
            self.__title = title
        else:
            raise ValueError("Не указано название")


    @staticmethod
    # проверка на обязательность ввода названия
    def check_title(title):
        if title:
            return True
        else:
            return False


    @property
    def title(self):
        return self.__title


    @title.setter
    # сеттер для возможности ввода нового названия
    def title(self, new_title):
        if Food.check_title(new_title):
            self.__title = new_title
        else:
            raise ValueError("Не ввели название")



class Product(Food):

    def __init__(self, title, caloric, cost):
        super().__init__(title)

        if Product.check_value(caloric):
            self.__caloric = int(caloric)
        else:
            raise ValueError("Неверно введены калории")

        if Product.check_value(cost):
            self.__cost = int(cost)
        else:
            raise ValueError("Неверно введена цена")


    @staticmethod
    def check_value(value):
        if str(value).isnumeric():  # проверка на наличие
            return int(value) >= 0  # проверка на положительное. (0 ввести можно)
        else:
            return False


    @property
    def caloric(self):
        return self.__caloric


    @caloric.setter
    # сеттер для возможности ввода нового значения
    def caloric(self, new_caloric):
        if Product.check_value(new_caloric):
            self.__caloric = new_caloric
        else:
            raise ValueError("Неверно ввели калории")


    @property
    def cost(self):
        return self.__cost


    @cost.setter
    # сеттер для возможности ввода нового значения
    def cost(self, new_cost):
        if Product.check_value(new_cost):
            self.__cost = new_cost
        else:
            raise ValueError("Неверно ввели цену")



class Ingredient():

    def __init__(self, Product, weight):
        self.metaclass = Product

        if Product.check_value(weight):
            self.__weight = int(weight)
        else:
            raise ValueError("Неверно введен вес")


    @property
    def weight(self):
        return self.__weight


    @weight.setter
    # сеттер для возможности ввода нового значения
    def weight(self, new_weight):
        if Product.check_value(new_weight):
            self.__weight = new_weight
        else:
            raise ValueError('Неверно ввели вес')


    def get_caloric(self):
        face_cal = self.metaclass.caloric * self.__weight / 100
        return face_cal


    def get_cost(self):
        face_cos = self.metaclass.cost * self.__weight / 100
        return face_cos



class Pizza(Ingredient, Product):

    def __init__(self, title, ingredients):
        super(Product, self).__init__(title)

        self.ingredients = ingredients


    def total_caloric(self):
        total_caloric = 0
        for ingredient in self.ingredients:
            total_caloric += ingredient.get_caloric()

        return float(total_caloric)


    def total_cost(self):
        total_cost = 0
        for ingredient in self.ingredients:
            total_cost += ingredient.get_cost()

        return float(total_cost)


    def __str__(self):
        return f'{self.title} ({self.total_caloric()} kkal). Цена: {self.total_cost()} руб.'



# создаем продукты с указанием названия, калорийности продукта и его себестоимости
dough_product = Product('Тесто', 200, 20)
tomato_product = Product('Помидор', 100, 50)
cheese_product = Product('Сыр', 100, 120)

# Из продуктов создаем ингредиенты. Для каждого указываем продукт,
# из которого он состоит и вес продукта
douth_ingredient = Ingredient(dough_product, 100)
tomato_ingredient = Ingredient(tomato_product, 100)
cheese_ingredient = Ingredient(cheese_product, 100)

# из ингредиентов создаем пиццу
pizza_margarita = Pizza('Маргарита', [douth_ingredient, tomato_ingredient, cheese_ingredient])

# выводим экземпляр пиццы
print(pizza_margarita)
