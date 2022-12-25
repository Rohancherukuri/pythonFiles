# Multiprocessing in python 
import multiprocessing as mp 
import time 

start  = time.perf_counter()

def task():
    print("Sleeping for 1 second...")
    time.sleep(1)
    print("Done sleeping...")

p1 = mp.Process(target = task)
p2 = mp.Process(target = task)

p1.start()
p2.start()

p1.join()
p2.join()

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")