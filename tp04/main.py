from Rectangle import Rectangle
from DataRectangle import DataRectangle

def main():
    r = Rectangle(6,4)
    r1 = Rectangle(6,4)
    
    print(r.longueur)
    assert r.longueur == 6
    print(r.largeur)
    assert r.largeur == 4
    
    r.longueur = 12
    print(r.longueur)
    assert r.longueur == 12
    assert r.surface == 48
    
    s = str(r)
    print(s)

    r2 = Rectangle(6,4)
    r3 = Rectangle(6,4)
    print("cpt r1",r1.get_cpt())
    print("cpt",Rectangle.get_cpt())
    
    # if r2.__eq__(r3)
    if r2 == r3:
        print("ok")
    else:
        print("ko")

    print(50*'-')
    r4 = Rectangle()
    print(r4)
    r5 = Rectangle.build_from_str("6x3")
    print(r5)
    print(50*'-')
    r6 = DataRectangle(2,3)
    print(r6)
    print(r6.surface)
    print()
    print()
if __name__ == '__main__':
    main()
