from pprint import pprint
class A:
    def __init__(self,v) -> None:
        self.value = v
    
    def the_method(self):
        print(f"The method A {self.value=} {self.__class__.__name__}")

class B(A):
    def __init__(self,v) -> None:
        self.value = v
    
    def the_method(self):
        print(f"The method B {self.value=} {self.__class__.__name__}")


class C(A):
    def __init__(self,v) -> None:
        self.value = v
    
    def the_method(self):
        
        print(f"The method C {self.value=} {self.__class__.__name__}")


class D(C,B):
    def __init__(self,v) -> None:
        self.value = v
    
    def the_method(self):
        super(C,self).the_method()
        super(B,self).the_method()
        print(f"The method D {self.value=} {self.__class__.__name__}")



def main():
    d = D(1)
    d.the_method()

    pprint(D.mro()) # method resolution order

if __name__ == '__main__':
    main()
