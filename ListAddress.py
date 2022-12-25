# Printing the memory address of items in the list

def printMemory(l):
    memory = []
    for i in l:
        memory.append(id(i))
    return memory

if __name__ == "__main__":
    mylist = [i for i in range(1,11)]
    
    p = printMemory(mylist)
    
    print("The original list is: ",mylist)
    print("THe memory addresses of the list is: \n",p)
    
     