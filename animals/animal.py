import dataclasses as dc


@dc.dataclass
class Animal:
    name: str
    type: str

    def make_noise(self):
        pass


@dc.dataclass
class Frog(Animal):
    def make_noise(self):
        return "Kwaak..."


@dc.dataclass
class Pinguin(Animal):
    def make_noise(self):
        return "KeKwaak!"


@dc.dataclass
class Snake(Animal):
    def make_noise(self):
        return "SSssss python ssss"

