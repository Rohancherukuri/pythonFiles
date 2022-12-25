# Practicing lambda functions
f = lambda x: x+2
if __name__ == "__main__":
    x = float(input("Enter a number: "))
    result = f(x)
    print("The result is: %.2f"%result)