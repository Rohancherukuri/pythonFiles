# Tutorial on list comprehensions,for loops and while loops

x = [1,2,3,4,5]
y = []

# Squaring the elements of the list using while loop as iterator
i = 0
while i < len(x):
    print(x[i]**2)
    i = i + 1

print("*"*10)

# Squaring the elements of the list using for loop as iterator
for j in x:
    print(j**2)

print("*"*10)

# Squaring the elements of the list using list comprehension as iterator
y = [k**2 for k in x]
print(y)
    
