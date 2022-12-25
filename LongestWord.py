# Finding longest word in python in a given list

def long_word(l,n):
    for i in l:
        if len(i)>n:
            print(i)
long_word(["Rohan","Madhavi","Suresh","Likith","Omkar","Naveen","Poorna","Sai","Unnendhra"],5)
