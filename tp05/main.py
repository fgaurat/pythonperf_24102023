from Rectangle import Rectangle
from Carre import Carre
from Cercle import Cercle
from ICalcGeo import ICalcGeo

def show_surface(o:ICalcGeo):
    print("surface",o.surface,type(o))

def main():
    r = Rectangle(4,3)
    c = Carre(4)
    print("surface carre",c.surface)
    print(c)
    c.cote = 12
    print("carre",c)
    print("surface carre",c.surface)
    show_surface(r)
    show_surface(c)
    print(50*'-')

    ce = Cercle(3)
    print("ce.surface",ce.surface)
    print()
    print()
    # i = ICalcGeo()

if __name__ == '__main__':
    main()
