import dataclasses as dc


@dc.dataclass
class Food:
    name: str
    price: float
    cals: int

