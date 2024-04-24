import numpy as np

# 2D list 
a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
print ("Normal 2D array:")
print (a)

# Numpy array 
A = np.array(a)
print ("Numpay 2D array")
print (A)
print ("The Dimention of A:",A.ndim)
print ("The Shape of A:",A.shape)
print ("The Size of A:",A.size)

# Accessing different elements
print (A[1, 2])
print (A[1][2])
print (A[0][0:2])
print ("Column Slicing:")
print (A[0:2, 2])

# Basic Operations
X = np.array ([[1, 0], [0, 1]])
print ("X",X)
Y = np.array ([[2, 1], [1, 2]])
print ("Y",Y)

Z = X + Y
print ("Sum:")
print (Z)

print ("2*Y:")
print (2*Y)

M = X * Y
print ("Multiplication:")
print (M)

# Creating  a Matrix
A = np.array ([[0, 1, 1],[1, 0, 1]])
print ("Matrix A:")
print (A)

B = np.array ([[1, 1], [1, 1], [-1, 1]])
print ("Matrix B:")
print (B)

C = np.array ([[1, 1], [2, 2], [3, 3]])
print ("Matrix C:")
print (C)

print ("Transpose of C:")
print (C.T)

# Dot product
Z = np.dot (A, B)
print ("Dot product:")
print (Z)

print (np.sin(Z))

# Excercise 
# 1. Consider the following list a, convert it to Numpy Array.
a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
A = np.array (a)
print (A)

# 2. Calculate the numpy array size.
print ("Size of the Array:", A.size)

# 3. Access the element on the first row and first and second columns.
print ("The element on frist row and first and second column is:", A[0, 0:2])

# 3. Perform matrix multiplication with the numpy arrays A and B.
B = np.array([[0, 1], [1, 0], [1, 1], [-1, 0]])

M = np.dot (A, B)
print ("Matrix Multiplication of Matrix A and B is:")
print (M)

# Completed