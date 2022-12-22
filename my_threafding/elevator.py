import threading
import time
from threading import Thread
from threading import Lock


lift_state = 0
pos = []


def elevator():
    global lift_state, pos

    def run_lift():
        global lift_state, pos
        state = tuple(pos)
        if state[1] == "up":
            for lift in range(lift_state + 1, state[0] + 1):
                print(f"Elevator in {lift} th floor")
                time.sleep(5)
                print(threading.current_thread().name)
            lift_state = state[0]
        elif state[1] == "down":
            for lift in range(lift_state, state[0] - 1, -1):
                print(f"Elevator in {lift} th floor")
                time.sleep(5)
            lift_state = state[0]
        else:
            for lift in range(lift_state - 1, -1, -1):
                print(f"Elevator in {lift} th floor")
                time.sleep(1)
            lift_state = 0
    flag = True
    while flag:
        floor = input("Floor number : ")
        if floor.isdigit():
            if lift_state < int(floor) < 11:
                pos = [int(floor), "up"]
                run_lift()
            elif 11 > int(floor) < lift_state:
                pos = [int(floor), "down"]
                run_lift()

        else:
            print("lift not working...")
            break


if __name__ == '__main__':
    thread = Thread(target=elevator, name='thread_1')
    thread.start()
    thread.join()

