import torch
from torch.utils.tensorboard import SummaryWriter
import torchvision
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from time import time

class Net(nn.Module):
    def __init__(self):
        super(Net,self).__init__()
        self.conv1 = nn.Conv2d(1,6,5)
        self.pool = nn.MaxPool2d(2,2)
        self.conv2 = nn.Conv2d(6,16,5)
        self.fc1 = nn.Linear(16*4*4,120)
        self.fc2 = nn.Linear(120,84)
        self.fc3 = nn.Linear(84,10)
    
    def forward(self,x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1,16*4*4)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x
    
def main():
    net = Net()
    print(type(net))
    print(dir(net))
    
    
if __name__ == "__main__":
    try:
        t1 = time()
        main()
    except Exception as e:
        print("Sorry there was an error in your code: "+str(e))
        
    finally:
        t2 = time() - t1
        print("[Finished in: "+str(round(t2,3))+" sec]")