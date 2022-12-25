import tensorflow as tf
from time import time
import numpy as np
import warnings
warnings.simplefilter("ignore")

def main():
    try:
        mylist = [float(i) for i in range(np.random.randint(1,10))]
        tensor = tf.constant(mylist)
        print(type(tensor))
        print(tensor)
    
    except Exception as e:
        print(f"An error has occured in the main function: {e}")
    
if __name__ == "__main__":
    try:
        
        t1 = time()
        main()
    
    except (KeyboardInterrupt,Exception) as e:
        print(f"Sorry there was an error in your code: {e}")
    
    finally:
        t2 = time() - t1
        print(f"Finished in: {t2} sec")
        