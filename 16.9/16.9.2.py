# Make code which  describes the geometrical figure.
# Make class "rectangle" by the __init__ method.
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b


R = Rectangle(5, 15)

print(R.get_area())
