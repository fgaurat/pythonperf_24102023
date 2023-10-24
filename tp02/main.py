


def do_log(prefix="",enable=True):
    def wrapper_f(func):
        def wrapper(*args,**kwargs):
            if enable:
                print(f"{prefix} BEFORE",args,kwargs)
            r = func(*args,**kwargs)
            if enable:
                print(f"{prefix} AFTER",r)
            return r
        return wrapper
    return wrapper_f

@do_log("LOG",True)
def say_hello(name):
    r = f"Hello {name}"
    return r

@do_log('ADD',True)
def add(a,b):
    return a+b

def main():
    hello =say_hello(name="Fred")
    a = add(1,2)
    print(hello)
    print(a)



if __name__ == '__main__':
    main()
