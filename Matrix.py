# Constructing a matrix in python
R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 

# Initialize matrix 
matrix = [] 
print("Enter the entries rowwise:") 

# For user input 
for i in range(R):		 # A for loop for row entries 
	a =[] 
	for j in range(C):	 # A for loop for column entries 
		a.append(eval(input())) 
	matrix.append(a)
print("The matrix is: ")
# For printing the matrix 
for i in range(R): 
	for j in range(C): 
		print(matrix[i][j], end = " ") 
	print() 




