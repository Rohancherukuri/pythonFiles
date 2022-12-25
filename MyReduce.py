# Making my own reduce function in python

def add(x,y):
    return x+y

def fact(x,y):
    return x*y

def myreduce(func,l):
    first = l[0]
    for i in l[1::]:
        first = func(first,i)
    print(first)

myreduce(fact,[1,2,3,4,5])

