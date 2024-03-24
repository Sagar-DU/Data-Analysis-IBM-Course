# creating a list
# L = ["Michael Jackson", 10.1,  1982]

# print (L)

# # printing the elements on each index

# print ("The same element using negative and positive indexing:\n Negative:", L[0], "\n Positive:", L[-3])
# print ("The same element using negative and positive indexing:\n Negative:", L[1], "\n Positive:", L[-2])
# print ("The same element using negative and positive indexing:\n Negative:", L[2], "\n Positive:", L[-1])

# nested list
# L2 = L + [1, 2]
# L2.append(("A", 1))

# print (L2)

# print ("Sliced List:", L2[-2:])

# L.extend(["pop", 10])

# print ("Extended List:", L)

# L.append(("King", "Legend"))

# print ("Appended List:", L)

# changing list's element
# A = ["disco", 210, 1.2]
# print ("Before change:", A)

# A[0] = "Hard rock"
# print ("After change:", A)

# A = ["disco", 210, 1.2]
# print ("Before change:", A)

# del (A[-1])
# print ("After change:", A)

# splitedList = "Hard Rock".split()
# print ("Splited List:", splitedList)

# splitedByDelimiter = "A, B, C, D".split()
# print ("Splited by comma:", splitedByDelimiter)

# copy and cloning
# B = A # copying by referance

# print ("Before A:", A)
# print ("Before B:",B)

# copying by referance changes both when one is changed
# B[0] = "Bananna"

# print ("After A:", A)
# print ("After B:", B)

# cloning solves this problem
# B = A[:] # cloning process

# print ("Before A:", A)
# print ("Before B:", B)

# B[0] = "Bananna"

# print ("After A:", A)
# print ("After B:", B)

# Excercise
# 1. Create a list a_list, with the following elements 1, hello, [1,2,3] and True.
# a_list = [1, 'hello', [1, 2, 3,], True]
# print (a_list)

# 2. Find the value stored at index 1 of a_list.
# print (a_list[1])

# 3. Retrieve the elements stored at index 1, 2 and 3 of a_list.
# print (a_list[1:4])

# 4. Concatenate the following lists A = [1, 'a'] and B = [2, 1, 'd']:
# A = [1, 'a'] 
# B = [2, 1, 'd']
# print ("Concatenated A & B:", A + B)

# 5. At first we need to create a empty list for storing the items to buy in Shopping list.
shopping_list = []

# 6. Now store the number of items to the shopping_list
# Watch
# Laptop
# Shoes
# Pen
# Clothes
shopping_list = ["Watch", "Laptop", "Shoes", "Pen", "Clothes"]
# print (shopping_list)

# 7. Add a new item to the shopping_list
# Seems like I missed one item "Football" to add in the shopping list.
shopping_list.append("Football")
# print (shopping_list)

# 8. Print First item from the shopping_list
# Let's check the first item that we need to buy.
print ("First item:",shopping_list[0])

# 9. rint Last item from the shopping_list
# Let's check the last time that we need to buy.
print ("Last item:", shopping_list[-1])

# 10. Print the entire Shopping List
print ("Entire shopping list:", shopping_list)

# 11. Print the item that are important to buy from the Shopping List
# Print "Laptop" and "shoes"
print ("Important items:", shopping_list[1:3])

# 12. Change the item from the shopping_list
# Instead of "Pen" I want to buy "Notebook" let's change the item stored in the list.
shopping_list[3] = "Notebook"
print ("Changed list:", shopping_list)

# 13. Delete the item from the shopping_list that is not required
# Let's delete items that are unimportant, such as; I don't want to buy Clothes, let's delete it.
del(shopping_list[4])

# 14. Print the shopping list
# We are ready with our shopping list.
print ("New shorted shopping list:", shopping_list)

# Completed
