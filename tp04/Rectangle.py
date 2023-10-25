


class Rectangle:

    def __init__(self,longueur,largeur) -> None:
        self.__longueur = longueur
        self.__largeur= largeur

    @property
    def longueur(self):
        return self.__longueur
    
    @property
    def largeur(self):
        return self.__largeur

    @longueur.setter
    def longueur(self,l):
        if l<=0:
            raise Exception("longueur")
        self.__longueur = l
    
    @largeur.setter
    def largeur(self,l):
        if l<=0:
            raise Exception("largeur")

        self.__largeur =l
    
    @property
    def surface(self):
        return self.__longueur*self.__largeur
    
    def __del__(self):
        print("Rectangle def __del__(self)")

    # longueur = property(get_longueur,set_longueur,doc="propriété longueur")
    # largeur = property(get_largeur,set_largeur,doc="propriété largeur")
    # surface = property(get_surface,doc="propriété surface")