import dataclasses as dc


@dc.dataclass
class Circle:
    radius: int

    def circumference(self) -> float:
        return 2 * 3.14 * self.radius

    def area(self) -> float:
        return 3.14 * (self.radius ** 2)
