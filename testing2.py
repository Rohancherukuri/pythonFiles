from helping import Student

def fib(n):
    if n <= 1:
        return n # base condition
    
    else:
        return fib(n-1) + fib(n-2)

n_terms = int(input("Enter range term: "))
l = [fib(i) for i in range(n_terms)]
print(l)

n_range = int(input("Enter the number of objects to be created: "))
s_lst = []
for i in range(n_range):
    print("*"*40)
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    age = int(input("Enter the age: "))
    cgpa = float(input("Enter cgpa: "))
    rollno = input("Enter the rollno: ")
    year = int(input("Enter year: "))
    s_lst.append(Student(fname,lname,age,cgpa,rollno,year))
print()
print(s_lst)
for i in s_lst:
    i.show()

print("\nThe type of element present in the list is: "+str(type(s_lst[0])))