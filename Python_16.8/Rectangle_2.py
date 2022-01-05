from rectangle import Rectangle, Square, Circle

# Создаем два прямоугольника

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

# Вывод площади наших двух прямоугольников
print("Площадь первого прямоугольника:", rect_1.get_area())
print("Площадь вторго прямоугольника:", rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)

# Возводин в квадрат аши переменные

print("Квадрат первой переменной", square_1.get_area_square(),
      "Квадрат второй переменной", square_2.get_area_square())

circle_1 = Circle(5)
circle_2 = Circle(10)
# все объекты перенести в единую коллекцию
figures = [rect_1, rect_2, square_1, square_2, circle_2, circle_1]

# Внутри цикла проверяем:
#
# Если экземпляр класса figure является квадратом,
# то вызываем метод get_area_square().

# В противном случае — обрабатываем данные для прямоугольника методом get_area().

# isinstance, поддерживающая наследование. Она проверяет, является ли
# аргумент объекта экземпляром класса или экземпляром класса из кортежа
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    if isinstance(figure, Rectangle):
        print(figure.get_area())
    if isinstance(figure, Circle):
        print(figure.get_area_Circle())