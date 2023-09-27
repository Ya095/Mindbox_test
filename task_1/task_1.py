import math
from abc import ABC, abstractmethod


__all__ = ["Circle", "Triangle", "calculate_all_figures_area"]


class Figure(ABC):
    @abstractmethod
    def calculate_area(self, *args, **kwargs):
        pass


class Utils:
    @staticmethod
    def _check_length(*args):
        """ Проверка введенных размеров для фигур """

        for length in args:
            if not isinstance(length, (int, float)):
                raise TypeError("Размеры должны быть числовыми значениями.")
            elif length <= 0:
                raise ValueError("Размеры должны быть положительными числами > 0.")


class Circle(Figure, Utils):
    def __init__(self, radius):
        self._check_length(radius)
        self.radius = radius

    def calculate_area(self):
        """ Расчет площади круга """

        return math.pi * (self.radius ** 2)


class Triangle(Figure, Utils):
    def __init__(self, side1, side2, side3):
        self._check_length(side1, side2, side3)
        self.__is_triangle(side1, side2, side3)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def __sort_triangle_sides(self, *args):
        """ Сортировка сторон треугольника """

        sides = [*args]
        sides.sort()
        return sides

    def __is_triangle(self, side1, side2, side3):
        """ Проверка существования треугольника с заданными сторонами """

        sides = self.__sort_triangle_sides(side1, side2, side3)
        if not sides[0] + sides[1] > sides[2]:
            raise ValueError("Треугольник с заданными сторонами не существует.")

    def calculate_area(self):
        """ Расчет площади треугольника """

        p = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))

    def is_right_triangle(self):
        """ Проверка, является ли треугольник с заданными сторонами прямоугольным """

        sides = self.__sort_triangle_sides(self.side1, self.side2, self.side3)
        return (sides[0]**2 + sides[1]**2) == sides[2]**2


def calculate_all_figures_area(*args):
    Figure._check_length(*args)

    if len(args) == 1:
        return Circle(*args).calculate_area()
    elif len(args) == 3:
        return Triangle(*args).calculate_area()
    else:
        raise NotImplementedError(f"Метод расчета площади для {len(args)} аргументов не реализован!")


calk = Circle(1)
print(calk.)