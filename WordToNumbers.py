# Converting a words to numbers
import pandas as pd
from word2number import w2n
x = ['one','two','three','four','five']
df = pd.DataFrame(x)
print(df)
print()
l = []
for i in df[0]:
    l.append(w2n.word_to_num(i))
print(l)
print()
df = pd.DataFrame(l)
print(df)
print(type(df))

