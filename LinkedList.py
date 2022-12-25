from time import time
import numpy as np

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    """This is a LinkedList class implemented in python3"""
    def __init__(self):
        self.head = None
        
    def insert(self,val):
        newval = Node(val)
        newval.next = self.head
        self.head.next = newval
    
    def display(self):
        temp_list = []
        temp = self.head
        if temp == None:
            print("The LinkedList is empty!")
        else:
            while temp is not None:
                temp_list.append(temp.data)
                temp = temp.next
            print(temp_list)
            
    
    def search(self,key):
        temp = self.head
        self.key = key
        count = 0
        while(temp):
            if temp.data == self.key:
                return "Key "+str(self.key)+" is found at "+str(count)+" position."
            count += 1
            temp = temp.next
        else:
            return "Key not found"
                    
        
def main():
    l = LinkedList()
    l.head = Node(1)
    second = Node(2)
    third = Node(3)
    l.head.next = second
    second.next = third
    third.next = None
    l.display()
    key = eval(input("Enter the key element to be searched: "))
    print(l.search(key))
    """val = eval(input("Enter the element to be inserted: "))
    fourth = l.insert(val)
    print("After inserting: ")
    l.display()"""

if __name__ == "__main__":
    try:
        t1 = time()
        main()
    
    except (KeyboardInterrupt,Exception) as e:
        print("Sorry there was an error in your code: "+str(e))
    
    finally:
        t2 = time() - t1
        print("[Finished in: "+str(round(t2,3))+" sec]")