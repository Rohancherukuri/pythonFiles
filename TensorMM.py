from time import time
import torch

def main():
    tens1 = torch.tensor([[1,2,3],[4,5,6],[7,8,9]])
    tens2 = tens1    
    ans = torch.mm(tens1,tens2)
    print("The final result is: \n"+str(ans))
    
if __name__ == "__main__":
    try:
        t1 = time()
        main()
    
    except (KeyboardInterrupt,Exception) as e:
        print("Sorry there was an error in your code: "+str(e))
    
    finally:
        t2 = time() - t1
        print("[Finished in: "+str(round(t2,3))+" sec]")