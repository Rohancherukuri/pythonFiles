# This is a tensorflow tutorial
import tensorflow as tf
from time import time
from numba import jit
import warnings
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.simplefilter("ignore")

@jit
def summation(a,b):
    """ Adding the two tensors function
        Similarly we can perfrom other mathematical 
        operations such as subtratction,
        multiplication and division etc 
    """
    c = a + b
    return c

def main():
    """ The main function """
    print("The version of tensorflow we are using is: "+str(tf.__version__))
    x = tf.constant(4,shape = (1,1),dtype = tf.float32)
    print(x)
    print("The Identity matrix is: ")
    y = tf.eye(3,dtype = tf.int32)
    print(y)
    print("The standard normal distribution is: ")
    z = tf.random.normal((3,3),mean = 0,stddev = 1)
    print(z)
    print("The uniform distribution is: ")
    a = tf.random.uniform((1,3),minval = 0,maxval = 1)
    print(a)
    print("The range of the tensor is: ")
    b = tf.range(start = 0,limit = 11,delta = 2)
    print(b)
    print("Changing the tensor into float64: ")
    c = tf.cast(b,dtype = tf.float64)
    print(c)
    tensor1 = tf.constant([1,2,3])
    tensor2 = tf.constant([9,8,7])
    s = summation(tensor1,tensor2)
    print("The sum of two tensors is: "+str(s))
    print("The dot product of the two tensors is: ")
    result = tf.tensordot(tensor1,tensor2,axes = 1)
    print(result)
    print("The Another way of performing dotproduct of two tensors is: ")
    ans = tf.reduce_sum(tensor1 * tensor2,axis = 0)
    print(ans)
    print("The square of each element present in  the tensor is: ")
    exp = tensor1 **2
    print(exp)
    print("The matrix multiplication of two 2d tensors is: ")
    tensor3 = tf.random.normal((2,3))
    tensor4 = tf.random.uniform((3,4))
    #sol = tf.matmul(tensor3,tensor4)
    sol = tensor3 @ tensor4
    print(sol)
    # Tensor slicing operations
    print("Printing reverse of the tensor elements: ")
    const = tf.constant([1,2,3,4,5,6,7,8,9])
    print(const[::-1])
    # Gathering indecies
    print("Gathering indices of the tensor: ")
    indices = tf.constant([2,7])
    x_ind = tf.gather(const,indices)
    print(x_ind)
    print("Slicing through 2d tensor or multi-dimensional tensor: ")
    matrix = tf.constant([[1,2,3],
                          [4,5,6],
                          [7,8,9]])
    print(matrix[0:2,:])
    # Reshaping tensors
    print("Reshaping tensor: ")
    r = tf.reshape(const,(3,3))
    print(r)
    # Transposing the 2d tensor
    print("Transposing the 2d tensor: ")
    rt = tf.transpose(r,perm = [1,0])
    print(rt)
if __name__ == "__main__":
    try:
        t1 = time()
        main()
    
    except (KeyboardInterrupt,Exception) as e:
        print("Sorry there was an error in your code: "+str(e))
    
    finally:
        t2 = time() - t1
        print("[Finished in: "+str(round(t2,3))+" sec]")

