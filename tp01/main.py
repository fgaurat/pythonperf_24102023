import sys
import copy


if __name__ == "__main__":
    print("ok")

    print("Pythonfdsfsdfsd",sys.getrefcount("Pythonfdsfsdfsd"))
    a = "Python"
    print("Python",sys.getrefcount("Python"))
    print(a[0])
    # a[0] = "J"
    print(sys.getrefcount(2))
    b = 2
    print(sys.getrefcount(2))
    print(b,hex(id(b)))

    b = 3
    print(b,hex(id(b)))

    c = 3
    print(c,hex(id(c)))

    print('-'*50)
    la_liste=[10,20,30,40,50]
    print(la_liste)
    # la_liste_2 = la_liste.copy() # shallow
    la_liste_2 = la_liste[:]# shallow
    # la_liste[0]=1000
    
    print("la_liste",la_liste)
    print("la_liste_2",la_liste_2)

    l3 = la_liste[2:4]
    print(l3)
    l3[0]=1000
    print(l3)
    print(la_liste)
    print(50*'-')
    la_liste = [
        [10,20,30],
        [40,50,60],
        [70,80,90]
    ]
    print(la_liste)
    la_liste_2 = la_liste.copy() # => shallow
    la_liste_2 = copy.deepcopy(la_liste)
    la_liste[1][1] = 1000
    print("la_liste",la_liste)
    print("la_liste_2",la_liste_2)
