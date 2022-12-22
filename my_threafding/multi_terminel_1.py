import sys
import platform
from subprocess import Popen

messages = 'This is Console1', 'This is Console2'


def foo1():
    print("In foo1")
    i = input("Enter Something - ")
    print(i)
    input("Enter to exit")


def foo2():
    print("In foo2")
    i = input("Enter Something - ")
    print(i)
    input("Enter to exit")


def run_foo1():
    print("foo1 >>> Something")
    return "import sys; sys.path.append('path_to_your_program_folder'); from test_code import foo1; foo1()"


def run_foo2():
    print("foo2 >>> Something")
    return "import sys; sys.path.append('path_to_your_program_folder'); from test_code import foo2; foo2()"


# define a command that starts new terminal
if platform.system() == "Windows":
    new_window_command = "cmd.exe /c start".split()
else:  # XXX this can be made more portable
    new_window_command = "x-terminal-emulator -e".split()
if __name__ == '__main__':

    # open new consoles, display messages
    echos = [[sys.executable, "-c", run_foo1()],
             [sys.executable, "-c", run_foo2()]
             ]
    processes = [Popen(new_window_command + echo) for echo in echos]

    # wait for the windows to be closed
    for proc in processes:
        proc.wait()
