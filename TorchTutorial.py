from  time import time
import numpy
import torch

def main():
    """This is a main method"""
    
    print("This is a PyTorch tutorial")
    print("The PyTorch version we are using is: "+str(torch.__version__)+"\n")
    my_device = "cuda" if torch.cuda.is_available() else "cpu"
    my_tensor = torch.tensor([[1,2,3],[4,5,6],[7,8,9]],
                             dtype = torch.int64,
                             device = my_device)
    print("Tensor attributes:\n")
    print(my_tensor)
    print("")
    print(my_tensor.shape)
    print(my_tensor.dtype)
    print(my_tensor.device)
    print(my_tensor.requires_grad)
    print("Other initializing methods\n")
    print("Using torch.empty() method:")
    x = torch.empty(size = (3,3))
    print(x,"\n")
    print("Using torch.rand() method:")
    y = torch.rand((3,3))
    print(y,"\n")
    print("Using torch.eye() method:")
    z = torch.eye(5,5,dtype = torch.int64)
    print(z,"\n")
    print("Using torch.arange() method:")
    rangeTensor = torch.arange(start = 0,end = 11,step = 1)
    print(rangeTensor,"\n")
    print("Using torch.diag() method:")
    ones = torch.diag(torch.ones(3))
    print(ones,"\n")
    # Other ways of tensor initialization are:
    print("Other ways of tensor initialization are:\n")
    tensor = torch.arange(4)
    print(tensor.bool(),"\n")
    print(tensor.short(),"\n")
    print(tensor.long(),"\n")
    print(tensor.half(),"\n")
    print(tensor.float(),"\n")
    print(tensor.double(),"\n")
    
    # Array to Tensor conversions and vice versa
    print("Array to Tensor conversions and vice versa:\n")
    np_array = np.zeros((5,5))
    tensor_array = torch.from_numpy(np_array)
    print(tensor_array,"\n")
    np_array_back = tensor_array.numpy()
    print(np_array_back,"\n")
    

if __name__ == "__main__":
    try:
        t1 = time()
        main()
    
    except (KeyboardInterrupt,Exception) as e:
        print("Sorry there was an error in your code: "+str(e))
    
    finally:
        t2 = time() - t1
        print("\n")
        print("[Finished in: "+str(round(t2,3))+" sec]")
