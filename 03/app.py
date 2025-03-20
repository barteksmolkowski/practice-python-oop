class Employee:
    def __init__(self, name, position) -> None:
        self.name = name
        self.position = position

    def describe(self):
        return f"{self.name} pracuje na stanowisku {self.position}."


class Teacher(Employee):
    def __init__(self, name, position, subject) -> None:
        super().__init__(name, position)
        self.subject = subject

    def describe(self):
        return f"{self.name} jest nauczycielem i uczy {self.subject}."


class Doctor(Employee):
    def __init__(self, name, position=None) -> None:
        pos = position if position else self.__class__.__name__
        super().__init__(name, pos)

    def describe(self):
        return super().describe()


class Engineer(Employee):
    def __init__(self, name, position=None) -> None:
        pos = position if position else self.__class__.__name__
        super().__init__(name, pos)

    def describe(self):
        return super().describe()


if __name__ == "__main__":
    emp = Employee("Jan Kowalski", "Menedżer")
    print(emp.describe())

    doctor = Doctor("Anna Nowak")
    print(doctor.describe())
