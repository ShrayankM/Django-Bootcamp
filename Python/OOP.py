class Car:
    def __init__(self, make, year, model):
        self.make = make
        self.year = year
        self.model = model

    def display_features(self):
        print("Make:" + self.make)
        print("Year:" + str(self.year))
        print("Model:" + self.model)

class ElectricCar(Car):
    def __init__(self, make, year, model, range):
        super().__init__(make, year, model)
        self.range = range

    def display_Efeatures(self):
        self.display_features()
        print("Range: " + self.range)

# c = Car("Hyundia", 2003, "Santro")
# c.display_features()

# c = ElectricCar("Tesla", 2017, "Model3", "406 miles")
# c.display_Efeatures()


class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

c = Circle(3)
print(c.area())

#Special Methods
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

    def __len__(self):
        return self.pages


b = Book("Python", "Jose", 203)
print(b)
print(len(b))
