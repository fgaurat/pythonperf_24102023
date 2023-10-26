from Rectangle import Rectangle


class Test:

    def __new__(cls) -> None:
        print("__new__")
        return super().__new__(cls)

    # constructeur
    def __init__(self) -> None:
        print("__init__")

    def __call__(self, *args, **kwds):
        print("__call__")



def main():
    test = Test()
    test()
    r = Rectangle(1,2)
    print(r)
    r1 = Rectangle(3,6)
    print(hex(id(r)))
    print(hex(id(r1)))
    print(r)
    print(r1)

if __name__ == '__main__':
    main()
