from threading import Thread
from time import sleep

def threaded_function(arg):
    for i in range(arg):
        print("running")
        sleep(1)


if __name__ == "__main__":
    for i in range(10):

    print("thread finished...exiting")
