import traceback

# ZeroDivisionError => UpperCamelCase / PascalCase
# zeroDivisionError => camelCase
# zero_division_error => snake_case
# zero-division-error => kebab-case, train-case, spin-case

class DivBy12Error(Exception):

    def __init__(self) -> None:
        super().__init__("Division par 12 !!!")

def div(a, b):
    if b ==12:
        raise DivBy12Error()
    return a/b

def call_div(a, b):
    r=0
    try:
        print("open log")
        r = div(a, b)
    finally:
        print("close log")
    
    return r

def main():

    try:
        a = 3
        b = 12
        # b = int(input("valeur de b:"))
        # c = a/b
        c = call_div(a, b)
        print(c)
    except TypeError as e:
        print("TypeError", e)
    except ZeroDivisionError as e:
        print("ZeroDivisionError", e)
    except Exception as e:
        traceback.print_exc()
        print('Exception', e, type(e))
    else:
        print("pas d'erreur")

    print("la suite ...")


if __name__ == '__main__':
    main()
