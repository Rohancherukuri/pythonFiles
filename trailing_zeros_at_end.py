
def trailing_zeros(num):
    if num == 0:
        return 1

    elif int(num % 10) == 0:
        count = 0
        while int(num % 10) == 0:
            count += 1
            num = num // 10
        return count
    else:
        return 0

number = int(input("Enter a number: "))
output = trailing_zeros(number)
print(output)

