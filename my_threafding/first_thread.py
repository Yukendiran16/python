import threading


def cuber(n):
    print("Cube: {}".format(n * n * n))


def squarer(n):
    print("Square: {}".format(n * n))


if __name__ == '__main__':
    t1 = threading.Thread(target=squarer, args=(5,))
    t2 = threading.Thread(target=cuber, args=(5,))

    print(threading.active_count())
    # start the thread t1
    t1.start()
    print(threading.get_ident())
    t1.is_alive()
    print(t1.name)

    # start the thread t2
    t2.start()
    print(t2.daemon)
    print(threading.get_ident())
    print(threading.active_count())
    # wait until t1 is completed
    t1.join(timeout=1000000e93877363)
    # wait until t2 is completed
    t2.join(timeout=20)

    print(threading.main_thread())
    print(threading.enumerate())

    # both threads completed
    print("Done!")
