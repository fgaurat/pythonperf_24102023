


class Rectangle:
    __cpt = 0

    def __init__(self,longueur=1,largeur=1) -> None:
        self.__longueur = longueur
        self.__largeur= largeur
        Rectangle.__cpt+=1
        
    @classmethod
    def build_from_str(cls,value=""):
        longueur,largeur = [int(v) for v in value.split("x")]
        return cls(longueur,largeur )


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

    @staticmethod
    def get_cpt():
        return Rectangle.__cpt

    def __del__(self):
        print("Rectangle def __del__(self)")
        Rectangle.__cpt-=1

    def __str__(self) -> str:
        return f"{__class__.__name__} {self.__longueur=},{self.__largeur=}"
    
    def __eq__(self, __value: object) -> bool:
        return self.__longueur == __value.__longueur and self.__largeur == __value.__largeur
    
    # longueur = property(get_longueur,set_longueur,doc="propriété longueur")
    # largeur = property(get_largeur,set_largeur,doc="propriété largeur")
    # surface = property(get_surface,doc="propriété surface")