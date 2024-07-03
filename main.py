class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = self.__validate_color(color)
        self.__sides = self.__validate_sides(*sides)
        self.filled = False

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print("Некорректные значения RGB, цвет не изменён.")

    def set_sides(self, *new_sides):
        if self.is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            print("Некорректные значения сторон, стороны не изменены.")

    def get_sides(self):
        return self.__sides

    def __is_valid_color(self, r, g, b):
        return all(0 <= x <= 255 for x in (r, g, b))

    def __validate_color(self, color):
        if len(color) == 3 and self.__is_valid_color(*color):
            return list(color)
        else:
            return [0, 0, 0]  # если некорректные значения цвета, задаем черный цвет

    def is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.sides_count

    def __validate_sides(self, *sides):
        if self.is_valid_sides(*sides):
            return list(sides)
        else:
            return [1] * self.sides_count

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius):
        super().__init__(color, radius)
        self.__radius = radius

    def get_square(self):
        return 3.14 * (self.__radius ** 2)  # просто для примера, обычно используют math.pi


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        # Для простоты примера, тут могла бы быть реализация высоты треугольника


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length):
        super().__init__(color, *([side_length] * self.sides_count))
        self.side_length = side_length

    def get_volume(self):
        return self.side_length ** 3


# Проверка кода:
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())  # Вывод: [55, 66, 77]
print(cube1.get_color())  # Вывод: [222, 35, 130]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15)  # Изменится
print(cube1.get_sides())  # Вывод: [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
print(circle1.get_sides())  # Вывод: [15]

# Проверка периметра (круга), это и есть длина:
print(len(circle1))  # Вывод: 15

# Проверка объёма (куба):
print(cube1.get_volume())  # Вывод: 216