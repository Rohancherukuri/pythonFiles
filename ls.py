# Multiplication table list using list comprehension
from time import time

def main():
    try:
        num = int(input("Enter a number: "))
        end = int(input("Enter the range of the table: "))
        table = [num*i for i in range(end + 1)]

        print(f"The multiplication table of the given {num} is:")
        print(table)

        with open("tables.txt","a") as f:
            f.write("The Multipication Table\n")
            f.write(str(table))
            f.write("\n")
    except Exception as e:
        print(f"There was an error in your code: {e}")

if __name__ == "__main__":
    try:
        t1 = time()
        main()
    except (KeyboardInterrupt,Exception) as e:
        print(f"Sorry there was an error in your code: {e}")
    finally:
        t2 = time() - t1
        print(f"Finished in {t2} sec")