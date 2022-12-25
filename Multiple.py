# Implementing a multiple inheritance in python

class A:
    def show(self):
        print("Inside Class A")
    
class B:
    def disp(self):
        print("Inside Class B")

class C(A,B):
    def view(self):
        print("Inside Class C")

if __name__ == "__main__":
    try:
        c = C()
        c.show()
        c.disp()
        c.view()
    except(KeyboardInterrupt,Exception) as e:
        print("Sorry there was an error in your code: "+str(e))