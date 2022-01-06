# You need to write a program that allows you to list several.
# Solve the problem with a constructor method and apply one of the principles of inheritance.
class Guests:
    def __init__(self, name, city, ):
        self.name = name
        self.city = city

    def desc(self):
        return f"Name: {self.name}, city: {self.city}"


class New_guest(Guests):
    def __init__(self, name, city, status):
        super().__init__(name, city)
        self.status = status

    def get_all(self):
        return f" {self.name}, city: {self.city}, status: {self.status}"


a = New_guest("Daniel", "Prague", "Mentor")
person_1 = a.get_all()

b = New_guest("Alexander", "Moscow", "Mentor")
person_2 = b.get_all()
print(person_1)
print(person_2)