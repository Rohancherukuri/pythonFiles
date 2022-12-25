# Finding the length of the word in given list of characters

def length_word(l):
    m = map(lambda x:len(x),l)
    print(list(m))


length_word(["Rohan","Naveen","Uneendhra","Sai","Omkar","Likith","Poorna","Yuvraj","Murthi","Leela"])
