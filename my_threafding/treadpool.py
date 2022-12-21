from concurrent.futures import ThreadPoolExecutor
import threading
import random

result = 0


def task():
    print("Executing the given task")
    global result
    for i in range(10):
        result = result + i
    print("I: {}".format(result))
    print("The task is executed {}".format(threading.current_thread()))


def main():
    executor = ThreadPoolExecutor(max_workers=3)
    task1 = executor.submit(task)
    task2 = executor.submit(task)


if __name__ == '__main__':
    main()
