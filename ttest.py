def end_zeros(num):
    new_num = str(num)
    count = len(new_num) - len(new_num.rstrip("0"))
    return count

n = int(input("Enter a number: "))
o = end_zeros(n)
print(o)

