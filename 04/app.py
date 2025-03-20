from typing import TypeAlias

import numpy as np

AnimalList: TypeAlias = np.ndarray


class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def make_sound(self) -> str:
        return "Zwierzę wydaje dźwięk."


class Dog(Animal):
    def make_sound(self) -> str:
        return f"{self.name} szczeka: Hau! Hau!"


class Cat(Animal):
    def make_sound(self) -> str:
        return f"{self.name} miauczy: Miau! Miau!"


class Bird(Animal):
    def make_sound(self) -> str:
        return f"{self.name} miauczy: Miau! Miau!"


animals = np.array([Dog("Burek"), Cat("Mruczek"), Dog("Reksio")], dtype=object)

get_sounds = np.vectorize(lambda h: h.make_sound())

sounds_array = get_sounds(animals)

print(*sounds_array, sep="\n")
