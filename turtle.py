class Turtle:
    def __init__(self, name, age):
        self.cuteness = True
        self.name = name
        self.age = age

    def who(self):
        return f'"{self.name} is an awesome turtle who is {self.age} years old.'

    def one_year_passes(self):
        self.age += 1
        return self.who()

gary = Turtle("Gary", 100)
megan = Turtle("Megan", 23)
