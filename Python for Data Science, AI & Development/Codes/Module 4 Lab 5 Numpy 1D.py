import numpy as np

# Creating a numpy array 
a = np.array([0, 1, 3, 4, 5, 6])
print (type(a))

for index, count in enumerate(a):
    print("a[", count, "] = ", a[index])

print (np.__version__)
print (a.dtype)

b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])

print (type(b))
print (b.dtype)

c = np.array([20, 1, 2, 3, 4])
# Assigning new values
print (c)
c[0] = 100
print (c)
c[4] = 0
print (c)

# 1. Assign the value 20 for the second element in the given array.
a = np.array([10, 2, 30, 40,50])
print (a)
a[1] = 20
print (a)

# Slicing numpy array
d = c[1:4]
print (d)

c[3:5] = 300, 400
print ("New c", c)

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2]) # 1 is starting point 5 is ending point (5) excluded 2 is the number of steps

print(arr[:4])
print(arr[4:])
print(arr[1:5:])
print(arr[::2])

# 2. Print the even elements in the given array.
print(arr[1::2])

# Assigning Value with List
select = [0, 2, 3, 4]
print (select)
d = c[select]
print (d)

print (c)
c[select] = 1000
print (c)

# Basic array attributes 
print (a)
print (a.size)
print ("Max:",a.max())
print ("Min",a.min())
print ("Mean",a.mean())
print (a.ndim)
print (a.shape)

# 3. Find the size ,dimension and shape for the given array b
b = np.array([10, 20, 30, 40, 50, 60, 70])
print (b)
print (a.size)
print (b.ndim)
print (b.shape)

# Numpy Statistics 
a = np.array([1, -1, 1, -1])
print (a)
print (a.mean())
print (a.std())
b = np.array([-1, 2, 3, 4, 5])
print (b)
print ("Max:",b.max())
print ("Min",b.min())
print ("Mean",b.mean())

# 4. Find the sum of maximum and minimum value in the given numpy array
c = np.array([-10, 201, 43, 94, 502])
print (c)
print ("Max c:", c.max())
print ("Min c:", c.min())

# Numpy Array Operations
u = np.array([1, 0])
v = np.array([0, 1])

# Addition 
z = np.add(u,v)
print (z)

# Ploting 
import time
import sys
import matplotlib.pyplot as plt

''' def Plotvec1(u, z, v):
    
    ax = plt.axes() # to generate the full window axes
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)# Add an arrow to the  U Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(u + 0.1), 'u')#Adds the text u to the Axes 
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)# Add an arrow to the  v Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(v + 0.1), 'v')#Adds the text v to the Axes 
    
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')#Adds the text z to the Axes 
    plt.ylim(-0.05, 5)#set the ylim to bottom(-2), top(2)
    plt.xlim(-0.05, 5)#set the xlim to left(-2), right(2)
'''
# Plotvec1 (u, z, v)
# Showing plot
# plt.show()

# 5. Perform addition operation on the given numpy array arr1 and arr2:
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

sum = np.add (arr1, arr2)
print ("Addition:")
print (arr1)
print (arr2)
print (sum)

# Substraction 
a = np.array([10, 20, 30])
b = np.array([5, 10, 15])
c = np.subtract(a, b)
print ("Substraction:")
print (a)
print (b)
print (c)

# 6. Perform subtraction operation on the given numpy array arr1 and arr2:
substraction = np.subtract(arr1, arr2)
print (arr1)
print (arr2)
print (substraction)

# Array Multiplication 
x = np.array ([1, 2])
y = np.array ([2, 1])
z = np.multiply (x, y)
print ("Array Multiplication:")
print (x)
print (y)
print (z)
# Plotvec1 (x, z, y)
# plt.show()

# 7. Perform multiply operation on the given numpy array arr1 and arr2:
multi = np.multiply (arr1, arr2)
print (arr1)
print (arr2)
print (multi)
print (arr1.size, arr2.size, multi.size)

# Array Division 
c = np.divide (a, b)
print ("Array Division:")
print (a)
print (b)
print (c)

# 8. Perform division operation on the given numpy array arr1 and arr2:
div = np.divide (arr1, arr2)
print (arr1)
print (arr2)
print (div)

# Dot product
X = np.array ([1, 2])
Y = np.array ([3, 2])

Z = np.dot (X, Y)
print ("The dot product:")
print (X)
print (Y)
print (Z)

# 9. Perform dot operation on the given numpy array ar1 and ar2:
arr1 = np.array([3, 5])
arr2 = np.array([2, 4])
dot = np.dot (arr1, arr2)
print (arr1)
print (arr2)
print (dot)

# Adding Constant to a Numpy Array
u = np.array([1, 2, 3, -1])
print (u)
print ("u + 1:", u + 1)

# 10. Add Constant 5 to the given numpy array ar:
arr = np.array([1, 2, 3, -1])
print (arr)
print (arr + 5)

# Mathematical Functions
print ("The value of pi:",np.pi)

x = np.array([0, np.pi/2 , np.pi])
print (x)
y = np.sin(x)
print (y)

# Linspace
# Making up a numpy array within [-2, 2] and 5 elements
numLine = np.linspace(-2, 2, num=5)
print (numLine)
# Making a numpy array within [-2, 2] and 9 elements
numLine = np.linspace(-2, 2, num=9)
print (numLine)
# Making a numpy array within [0, 2π] and 100 elements 
x = np.linspace(0, 2*np.pi, num=100)
# print (x)
y = np.sin(x)
# print (y)
plt.plot(x, y)
# plt.show()

# 11. Make a numpy array within [5, 4] and 6 elements
numLine = np.linspace (5, 4, num = 6)
print (numLine)

# Iterating 1-D Arrays
arr1 = np.array([1, 2, 3])
print(arr1)

for x in arr1:
    print (x)

# 12. Implement the following vector subtraction in numpy: u-v
u = np.array([1, 0])
v = np.array([0, 1])
z = u - v
print (z)

# 13. Multiply the numpy array z with -2:
z = np.array([2, 4])
print (z)
print (z*2)

# 14. Consider the list [1, 2, 3, 4, 5] and [1, 0, 1, 0, 1]. Cast both lists to a numpy array then multiply them together:
a = np.array ([1, 2, 3, 4, 5])
b = np.array ([1, 0, 1, 0, 1])

c = np.multiply (a,b)
print (a)
print (b)
print (a*b)
print (c)

def Plotvec2(a,b):
    ax = plt.axes()# to generate the full window axes
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)#Add an arrow to the  a Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)#Add an arrow to the  b Axes with arrow head width 0.05, color blue and arrow head length 0.1
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)

# 15. Convert the list [-1, 1] and [1, 1] to numpy arrays a and b. Then, plot the arrays as vectors using the fuction Plotvec2 and find their dot product:
a = np.array ([-1, 1])
b = np.array ([1, 1])
Plotvec2 (a, b)
# plt.show()

# 16. Convert the list [1, 0] and [0, 1] to numpy arrays a and b. Then, plot the arrays as vectors using the function Plotvec2 and find their dot product:
print (u)
print (v)

Plotvec2 (u, v)
# plt.show()
print (np.dot (u, v))

# 18. Convert the list [1, 1] and [0, 1] to numpy arrays a and b. Then plot the arrays as vectors using the fuction Plotvec2 and find their dot product:
a = np.array ([1, 1])
b = np.array ([0, 1])
Plotvec2(a, b)
# plt.show()
print (a)
print (b)
print (np.dot (a, b))

# 19. Convert the list [1, 2, 3] and [8, 9, 10] to numpy arrays arr1 and arr2. Then perform Addition , Subtraction , Multiplication , Division and Dot Operation on the arr1 and arr2.
arr1 = np.array ([1, 2, 3])
arr2 = np.array ([8, 9, 10])

print (arr1)
print (arr2)
print ("Addition:", np.add (arr1, arr2))
print ("Subtraction:", np.subtract (arr1, arr2))
print ("Multiplication:", np.multiply (arr1, arr2))
print ("Division:", np.divide (arr1, arr2))
print ("Dot Product:", np.dot (arr1, arr2))

# 20. Convert the list [1, 2, 3, 4, 5] and [6, 7, 8, 9, 10] to numpy arrays arr1 and arr2. Then find the even and odd numbers from arr1 and arr2.
arr1 = np.array ([1, 2, 3, 4, 5])
arr2 = np.array ([6, 7, 8, 9, 10])

print ("Even numbers in array 1:", arr1[1::2])
print ("Even numbers in array 2:", arr2[::2])
print ("Odd numbers in array 1: ", arr1[::2])
print ("Odd numbers in array 2: ", arr2[1::2])