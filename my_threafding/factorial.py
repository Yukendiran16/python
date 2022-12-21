import threading
import time


def factorial(n):
    if n < 1:  # base case
        print("%s: %s" % ("Thread", threading.current_thread()))
        return 1
    else:
        returnNumber = n * factorial(n - 1)  # recursive call
        print(str(n) + '! = ' + str(returnNumber))
        return returnNumber


thread1 = threading.Thread(target=factorial, args=(5,)).start()
time.sleep(1)
threading.Thread(target=factorial, args=(5,)).start()

