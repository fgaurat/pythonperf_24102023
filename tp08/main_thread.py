import threading

lock = threading.Lock()

def traitement_long_1():
    with lock:
        for i in range(10):
            print(threading.current_thread().name,i)
    
    # lock est libéré
def traitement_long_2():
    with lock:
        for i in range(10):
            print(threading.current_thread().name,i)


def main():
    th1 = threading.Thread(target=traitement_long_1)
    th2 = threading.Thread(target=traitement_long_2)
    th1.start()
    th2.start()
    
    th1.join()
    th2.join()
    print("Terminé")

if __name__ == '__main__':
    main()
