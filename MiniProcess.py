# Creating sub processes
import multiprocessing as mp
from time import time, sleep
import torch
import warnings
import os
warnings.simplefilter("ignore")

class Parent:
    def __init__(self,struct):
        self.struct = struct
    
    def worker1(self):
        print("The Worker1 has started and the ID is: {}".format(os.getpid()))
        print("The worker1 job is: {}".format(self.struct))
        
    
    def worker2(self):
        print("The Worker2 has started and the ID is: {}".format(os.getpid()))
        print("The worker2 job is: {}".format(self.struct))


if __name__ == "__main__":
    try:
        print("The ID of main process is: {}".format(os.getpid()))
        mylist = [float(i) for i in range(11)]
        struct = torch.tensor(mylist)
        t1 = time()
        pt1 = Parent(struct)
        pt2 = Parent(struct)
        p1 = mp.Process(target = pt1.worker1)
        p2 = mp.Process(target = pt2.worker2)
        # Starting the processes
        p1.start()
        sleep(0.5)
        p2.start()
        print("The process ID of p1 is: {}".format(p1.pid))
        print("The process ID of p2 is: {}".format(p2.pid))
        # Checking the status of the processes
        print("Process p1 is alive: {}".format(p1.is_alive()))
        print("Process p2 is alive: {}".format(p2.is_alive()))  
	       
        # Joining the processes
        p1.join()
        p2.join()
        print("Both processes finished execution!")
        # check if processes are alive
        print("Process p1 is alive: {}".format(p1.is_alive()))
        print("Process p2 is alive: {}".format(p2.is_alive()))  
	       
    except (KeyboardInterrupt,Exception) as e:
        print("Sorry there was an error in your code: "+str(e))
    
    finally:
        t2 = time() - t1
        print("Finished in: {} sec".format(t2))