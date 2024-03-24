# creating a list
L = ["Michael Jackson", 10.1,  1982]

# print (L)

# # printing the elements on each index

# print ("The same element using negative and positive indexing:\n Negative:", L[0], "\n Positive:", L[-3])
# print ("The same element using negative and positive indexing:\n Negative:", L[1], "\n Positive:", L[-2])
# print ("The same element using negative and positive indexing:\n Negative:", L[2], "\n Positive:", L[-1])

# nested list
L2 = L + [1, 2]
L2.append(("A", 1))

# print (L2)

# print ("Sliced List:", L2[-2:])

L.extend(["pop", 10])

# print ("Extended List:", L)

L.append(("King", "Legend"))

# print ("Appended List:", L)

# changing list's element
# A = ["disco", 210, 1.2]
# print ("Before change:", A)

# A[0] = "Hard rock"
# print ("After change:", A)

A = ["disco", 210, 1.2]
# print ("Before change:", A)

# del (A[-1])
# print ("After change:", A)

splitedList = "Hard Rock".split()
# print ("Splited List:", splitedList)

splitedByDelimiter = "A, B, C, D".split()
# print ("Splited by comma:", splitedByDelimiter)

# copy and cloning
# B = A # copying by referance

# print ("Before A:", A)
# print ("Before B:",B)

# copying by referance changes both when one is changed
B[0] = "Bananna"

# print ("After A:", A)
# print ("After B:", B)

# cloning solves this problem
B = A[:] # cloning process

print ("Before A:", A)
print ("Before B:", B)

print ("After A:", A)
print ("After B:", B)