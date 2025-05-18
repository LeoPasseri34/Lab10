from dataclasses import dataclass

from model.country import Country


@dataclass
class Border:
    c1: Country
    c2: Country

    def __hash__(self):
        return hash((self.c1.CCode, self.c2.CCode))

    def __str__(self):
        return f"Border: {self.c1} - {self.c2}"