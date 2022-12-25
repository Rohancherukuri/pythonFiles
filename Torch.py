# Using pytorch library
import torch
import numpy


x1 = torch.tensor(np.array([i for i in range(1,11)]))
x2 = torch.tensor(np.array([i for i in range(10,20)]))

result = x1*x2
print(result)
print(type(result))