# Making my own filter function in python

def even(n):
    if n%2 == 0:
        return True

def myfilter(func,l):
    m = []
    for i in l:
        if func(i) == True:
            m.append(i)
    print(m)

myfilter(even,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
