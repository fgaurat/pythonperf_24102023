from collections import deque
def main():
    l = [10,20,30]
    print(l)

    l.append(40)
    print(l)
    last = l.pop()
    print(l)
    print(last)
    l.insert(0,0)
    print(l)
    first = l.pop(0)
    print(l)
    print(first)
    print(50*"-")
    l = [10,20,30]
    d = deque(l)
    print(d)
    d.appendleft(0)
    print(d)


if __name__ == '__main__':
    main()
