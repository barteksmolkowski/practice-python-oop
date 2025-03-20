class Person:
    def __init__(self, name, age, city) -> None:
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(
            f"Cześć, mam na imię {self.name}, mam {self.age} lat i mieszkam w {self.city}."
        )


Person("Jan", 25, "Warszawie").introduce()
Person("Anna", 30, "Krakowie").introduce()
Person("Piotr", 35, "Gdańsku").introduce()
