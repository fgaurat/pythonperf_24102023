
def build_function():

    l = "Python"
    def show_language():
        print("J'aime le",l)
    
    return show_language


def make_incrementor(i):

    def do_inc(value):
        return i+value
    
    return do_inc

def main():
    inc = make_incrementor(42)
    a = inc(0)# 42
    b = inc(1)# 43
    print(a)
    print(b)

def main_01():
    # functions are first class citizen
    my_function = build_function()
    my_function()


if __name__ == '__main__':
    main()
