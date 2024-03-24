# tuple1 = ("disco", 10, 1.2)
# print (type(tuple1))
# print ("Tuple:", tuple1)
# print ("Elements of Tuple:",tuple1[0])
# print ("Elements of Tuple:",tuple1[1])
# print ("Elements of Tuple:",tuple1[2])
# print ("Types of Tuple element:", type(tuple1[0]))
# print ("Types of Tuple element:", type(tuple1[1]))
# print ("Types of Tuple element:", type(tuple1[2]))
# # They can also access with negative index like string and list 

# # We can concatenate or combine tuples by using the + sign:
# tuple2 = tuple1 + ("hard rock", True)
# # print ("Concatinated Tuple:", tuple2)

# # We can slice tuples, obtaining new tuples with the corresponding elements:
# print ("Sliced tuple:", tuple2[1:5])

# # We can obtain the length of a tuple using the length command:
# print ("Length of the second tuple:", len(tuple2))

# Sorting
# Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2, 4, 3, 1)

# sortedRatings = sorted (Ratings)
# print ("Unsorted Ratings:", Ratings)
# print ("Sorted Ratings:", sortedRatings)

# A tuple can contain another tuple as well as other more complex data types. This process is called 'nesting'. Consider the following tuple with several elements:
# NestedT = (1, 2, ("pop", "rock"), (3, 4), ("disco", (1, 2)))
# print ("This is a nested tuple:", NestedT)
# print ("Element 0 of Tuple:", NestedT[0])
# print ("Element 1 of Tuple:", NestedT[1])
# print ("Element 2 of Tuple:", NestedT[2])
# print ("Element 2, 0 of the Tuple is:", NestedT[2][0])
# print ("Element 2, 1 of the Tuple is:", NestedT[2][1])
# print ("Element 3 of Tuple:", NestedT[3])
# print ("Element 3, 0 of the Tuple is:", NestedT[3][0])
# print ("Element 3, 1 of the Tuple is:", NestedT[3][1])
# print ("Element 4 of Tuple:", NestedT[4])
# print ("Element 4, 0 of the Tuple is:", NestedT[4][0])
# print ("Element 4, 1 of the Tuple is:", NestedT[4][1])
# print ("Element 4, 1, 0 of the Tuple is:", NestedT[4][1][0])
# print ("Element 4, 1, 1 of the Tuple is:", NestedT[4][1][1])

# Tuples are immutable. So, their elements cannot be changed like string and list 

# Excercis
genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", "R&B", "progressive rock", "disco")

# 1. Find the length of the tuple, genres_tuple:
print ("Tuple:", genres_tuple)
print ("Length of the Tuple:", len(genres_tuple))

# 2. Access the element, with respect to index 3:
print ("The elemet 0 of Tuple:", genres_tuple[-8])
print ("The elemet 1 of Tuple:", genres_tuple[-7])
print ("The elemet 2 of Tuple:", genres_tuple[-6])
print ("The elemet 3 of Tuple:", genres_tuple[-5])
print ("The elemet 4 of Tuple:", genres_tuple[-4])
print ("The elemet 5 of Tuple:", genres_tuple[-3])
print ("The elemet 6 of Tuple:", genres_tuple[-2])
print ("The elemet 7 of Tuple:", genres_tuple[-1])

# 3. Use slicing to obtain indexes 3, 4 and 5:
print ("Element of index 3, 4 and 5:", genres_tuple[3:6])

# 4. Find the first two elements of the tuple genres_tuple:
print ("First two element of the Tuple:", genres_tuple[:2])

# 5. Find the index of 's' in "disco":
print ("Printing the s in disco:", genres_tuple[7][2])

# 6. Generate a sorted List from the Tuple C_tuple=(-5, 1, -3):
C_tuple=(-5, 1, -3)
sortedTuple = sorted (C_tuple)
print ("Unsorted Tuple:", C_tuple)
print ("Sorted Tuple:", sortedTuple)