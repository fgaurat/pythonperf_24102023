

class SingletonMeta(type):
    
    instance = None       # Attribut statique de classe
    
    def __call__(self,*args,**kwargs): 
        """méthode de construction standard en Python"""
        if self.instance is None:
            self.instance = super(SingletonMeta,self).__call__(*args,**kwargs)
        return self.instance
    