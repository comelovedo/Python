# Make a class of geometrical figure where on output we will get the characteristics.
# It must has the attributes of the figure.
# Additionally, you must provide these attributes when you create the class object.


class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle({self.x}, {self.y}, {self.width}, {self.height})"


Rec = Rectangle(5, 10, 50, 100)
print(Rec)