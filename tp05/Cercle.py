from ICalcGeo import ICalcGeo
import math


class Cercle(ICalcGeo):

    def __init__(self, rayon=1) -> None:
        print(f"Cercle def __init__(self, {rayon})")
        self.__rayon = rayon

    @property
    def rayon(self):
        return self.__rayon

    @rayon.setter
    def rayon(self, rayon):
        self.__rayon = rayon

    @property
    def surface(self):
        return math.pi * self.__rayon**2

    def __str__(self) -> str:
        return f"{__class__.__name__} {self.__rayon=}"

    def __del__(self):
        print("Cercle def __del__(self)")
