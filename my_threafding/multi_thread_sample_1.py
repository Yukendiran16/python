import sys
import time
import multiprocessing
import threading


class MockStdin:
    def __init__(self):
        self.queue = None
        self.real_stdin = sys.stdin
        self.relay_process = None

    def readline(self):
        # when input() is called, it calls this function
        return self.queue.get()

    def writeline(self, s):
        # for input from elsewhere in the program
        self.queue.put(s)

    def relay_stdin(self):
        # for input from the user
        my_stdin = open(0)  # this is a new process so it needs its own stdin

        try:
            while True:
                inp = my_stdin.readline()
                self.queue.put(inp)
        except KeyboardInterrupt:
            # when killed, exit silently
            pass

    def __enter__(self):
        # when entering the `with` block, start replace stdin with self and relay real stdin
        self.queue = multiprocessing.Queue()

        self.relay_process = multiprocessing.Process(target=self.relay_stdin)
        self.relay_process.start()
        sys.stdin = self

    def __exit__(self, exc_type=None, exc_val=None, exc_tb=None):
        # when exiting the `with` block, put stdin back and stop relaying
        sys.stdin = self.real_stdin

        self.relay_process.terminate()
        self.relay_process.join()

    def __getstate__(self):
        # this is needed for Windows - credit to Leonardo Rick for this fix
        self_dict = self.__dict__.copy()
        del self_dict['real_stdin']
        return self_dict


def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=fn, args=args, kwargs=kwargs, daemon=True)
        thread.start()
        return thread

    return wrapper


if __name__ == '__main__':
    mock = MockStdin()


    @threaded
    def answer():
        time.sleep(2)
        # use mock to write to stdin
        mock.writeline('to be inputed')


    answer()

    with mock:
        # inside `with` block, stdin is replaced
        x = input('insert a value: ')
        print(f'\nvalue inserted: {x}')

    answer()

    # __enter__ and __exit__ can also be used
    mock.__enter__()
    x = input('insert a value: ')
    print(f'\nvalue inserted: {x}')
    mock.__exit__()

    # now outside the `with` block, stdin is back to normal
    x = input('insert another (stdin should be back to normal now): ')
    print(f'value inserted: {x}')
