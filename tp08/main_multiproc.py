import os
from multiprocessing import Pool
import time

def f(x):
    t=1
    start = time.time()
    while time.time()-start<t:
        pass
    
    return x*x

def main():

    start = time.time()
    print(os.cpu_count())
    with Pool(155) as p:
        print(p.map(f, range(1,130)))
    print(time.time()-start)


if __name__ == '__main__':
    main()
