from Rectangle import Rectangle
from Carre import Carre

def show_surface(o:Rectangle):
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


if __name__ == '__main__':
    main()
