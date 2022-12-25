# Testing the evaluate function
from plotly.express import scatter_3d
from pandas import DataFrame
from torch import tensor
from numpy import array
from time import time
def main():
    """This is main method"""
    try:
        data = {"Name":["Rohan","Poorna","Naveen","Sai","Likith","Omkar","Rishikesh","Murthi","Vamshi","Gana","Leela","Harsha","SaiUday","Spyder","Venkat"],
             "StrikeRate":[87,79,71,31,1,24,83,87,37,66,68,71,87,79,82],
             "NotOutRate":[12,21,39,67,98,69,31,72,55,80,54,99,26,19,17]}
        fig = scatter_3d(x = data["StrikeRate"],y = data["NotOutRate"],z = [i for i in range(15)])
        var = eval(input("Enter the value: "))
        print(type(var))
        print(var)
        if var is fig:
            var.show()
    except (KeyboardInterrupt,Exception) as e:
        print("An ERROR  occured: "+str(e))
        
if __name__ == "__main__":
    try:
        t1 = time()
        main()
        t2 = time()
    
    except (KeyboardInterrupt,Exception) as e:
        print("Sorry there was an error in your code: "+str(e))
    
    finally:
        t3 = t2 - t1
        print("[Finished in: "+str(round(t3,3))+" sec]")