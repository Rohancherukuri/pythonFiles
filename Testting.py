# Testing the oop concepts in python
import time as tm
class Square:
    start_time = tm.time()
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    
    def volume(self):
        self.vol = self.length * self.breadth
        return self.vol
    
    def display(self):
        finish_time = tm.time() - Square.start_time
        print("The Volume of the Square is: {}".format(self.vol))
        print("Total time taken to execute the Square class is: {} sec".format(finish_time))
    
if __name__ == "__main__":
    try:
        l = float(input("Enter the length of the square: "))
        b = float(input("Enter the breadth of the square: "))
        s = Square(l,b)
        s.volume()
        s.display()
    except Exception as e:
        print("Sorry an error occured in your code: "+str(e))
        
        