
import torch

def privateInformation(a,b):
    return a+b

if __name__ == "__main__":
    try:
        a = torch.tensor(int(input("Enter a number1: ")))
        b = torch.tensor(int(input("Enter a number2: ")))
        p = privateInformation(a,b)
        print("The Sum is: "+str(p))
    except (KeyboardInterrupt,Exception) as e:
        print("There was an error.")