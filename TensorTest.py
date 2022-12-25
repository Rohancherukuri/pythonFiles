# Iterating over a tensor
from torch import tensor

t = tensor([int(i) for i in input("Enter the elements into the tensor: ").split(",")])
print("The tensor elements contain: "+str(t))

# Looping over a tensor
 
'''for i in t:
     print(i)'''
print(t.size())