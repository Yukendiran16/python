import threading
from threading import Thread, Semaphore
from time import sleep
import multiprocessing
import concurrent.futures
import time
from concurrent.futures import ThreadPoolExecutor

lock = Semaphore()
x = 0

start = time.time()


def add_one():
    global x, lock
    for i in range(10):
        lock.acquire()
        x = x + 1
        print(threading.current_thread())
        lock.release()


def subtract_one():
    global x, lock
    for i in range(10):
        lock.acquire()
        x = x - 1
        print(threading.current_thread())
        lock.release()
    print(x)


# add_one()
# subtract_one()
print("The total time is :{0}".format(time.time() - start))

thread2 = Thread(target=subtract_one)
thread1 = Thread(target=add_one)
thread1.start()
thread2.start()

thread1.join()
thread2.join()

start = time.time()
print(x)
print("The total time is :{0}".format(time.time() - start))
#
# star = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print(threading.current_thread())
    return f'Done Sleeping...{seconds}'


with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    results = executor.map(add_one, range(20))
    # add_one()
    # subtract_one()
    # add_one()
    # subtract_one()
    # subtract_one()
    # add_one()

# with ThreadPoolExecutor(max_workers=3) as execute:
#     add_one()
#     subtract_one()
#     add_one()
#     subtract_one()
#     subtract_one()
#     add_one()
#     print("The total time is :{0}".format(time.time() - start))
#
#     for result in results:
#         print(result)
#
#     threads = []
#
#     for _ in range(10):
#         t = Thread(target=do_something, args=[1.5])
#         t.start()
#         threads.append(t)
#     print(threading.enumerate())
#     for thread in threads:
#         thread.join()
print(threading.enumerate())
finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')
