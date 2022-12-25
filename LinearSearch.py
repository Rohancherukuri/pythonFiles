# Implementing linear search in python

def search(l,key):
    for i in range(len(l)):
        if l[i] == key:
            print("The key element {} was found at {} position in the given list".format(key,i))
            break
    else:
        print("The key element {} was  not found in the given list".format(key))

if __name__ == "__main__":
    try:
        mylist = [eval(i) for i in input("Enter the elements: ").split(",")]
        key = eval(input("Enter a key element to be searched: "))
        print("Gven list is: {} and given key is: {}".format(mylist,key))
        search(mylist,key)
    except(KeyboardInterrupt,Exception) as e:
        print("Sorry there was an error in your code "+str(e))