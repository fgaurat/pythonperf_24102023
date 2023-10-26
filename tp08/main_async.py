import asyncio
import time
import threading


async def add(a,b):
    print(threading.current_thread().name)
    await asyncio.sleep(1)
    return a+b

async def main():
    r = add(1,3)
    r1 =  add(4,5)
    r2 =  add(42,54)
    r3 =  add(2,45)
    all = [r,r1,r2,r3]
    result = await asyncio.gather(*all)    
    print(result)


if __name__ == '__main__':
    
    asyncio.run(main())
