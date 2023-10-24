
def main():

    tofind = 35
    for i in range(10):
        print(i)
        if i == tofind:
            break
    else:
        print("pas trouvé")
    
    print("après la loop")
if __name__ == '__main__':
    main()
