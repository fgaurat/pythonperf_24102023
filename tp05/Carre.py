from Rectangle import Rectangle


class Carre(Rectangle):
    

    def __init__(self, cote=1) -> None:
        super().__init__(cote, cote)
        print(f"Carre def __init__(self, {cote})")
        self.__cote = cote
    
    @property
    def cote(self):
        return self.__cote
    
    @cote.setter
    def cote(self,cote):
        self.longueur = cote
        self.largeur = cote
        self.__cote=cote
    
    
    def __str__(self) -> str:
        return f"{__class__.__name__} {self.__cote=}"

    
    def __del__(self):
        print("Carre def __del__(self)")