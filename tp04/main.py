from Rectangle import Rectangle

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

if __name__ == '__main__':
    main()
