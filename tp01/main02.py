

def add(*l): # reducer
    print(l)
    r = 0

    for i in l:
        r+=i
    
    return r


def hello(**d):
    print(d)

# def the_function(param1,param2,/): # pos only
def the_function(*,param1,param2): # pos only
    print("the_function",param1,param2)

def main():

    l = [1,2,3,4]
    # r = add(l)

    r = add(1,2,3,4)
    print(r) # 10
    
    # r = add(l) # add([1,2,3,4])
    r = add(*l) # add(1,2,3,4)
    print(r) # 10
    print(50*'-')
    l = [1,2,3,4]
    a,b,c,d = l
    print(a,b,c,d)
    # a,b,c,d,e = l
    # print(a,b,c,d,e)
    a,b,*c = l
    print(a,b)
    print(c)
    print(50*'-')
    hello(name="GAURAT",first_name="Fred")
    
    d = {
        "name":"GAURAT","first_name":"Fred"
    }

    hello(**d)# hello(name="GAURAT",first_name="Fred")

    # s1 = "valeur 1 : {},valeur 2 : {}".format(l[0],l[1])
    s1 = "valeur 1 : {0},valeur 2 : {1}".format(*l)
    s2 = "valeur 1 : {name},valeur 2 : {first_name}".format(**d)
    print(s1)
    print(s2)
    print(50*'-')
    # the_function(1,2)
    # the_function(param1=1,param2=2)


if __name__ == '__main__':
    main()
