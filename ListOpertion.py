# Using List comprehension in python
import Key

if __name__ == "__main__":
    try:
        x = [int(i) for i in input("Enter only numbers: ").split(",")]
        l = [int(i) if i > 0 else 0 for i in x]
        # Making a list generator in python
        g = (i for i in range(1,11) if i%2 == 0)
        print(g)
        print("The list is: {}".format(l))
        print("-"*30)
        for j in g:
            print(j)
        print("-"*30)
        mylist = [eval(i) for i in input("Enter input elements: ").split(",")]
        for i in mylist:
            print(i)
    except(KeyboardInterrupt,Exception) as e:
        print("Sorry there was an error in your code"+str(e))
        