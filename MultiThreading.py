# Multi Threadding in python
import time
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            time.sleep(1)
class World(Thread):
    def run(self):
        for i in range(5):
            print("World")
            time.sleep(1)
if __name__ =="__main__":
    obj1 = Hello()
    obj2 = World()
    obj1.start()
    time.sleep(0.2)
    obj2.start()
    obj1.join()
    obj2.join()
    print("Bye")
