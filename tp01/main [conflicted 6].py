

i = 5


def f2(i,value=[]): 
    value.append(i)
    print("f2",value)

def f(value=i):
    print("dans f",value)


def main():
    global i
    b=None
    i=4567
    print("main",i) # 4567
    if True:
        b=12
    
    print(b)
    f()
    print(50*'-')
    f2(1)# [1]
    f2(2)# [2] || [1,2]
    f2(3)


if __name__ == '__main__':
    main()
    print("après main",i)
