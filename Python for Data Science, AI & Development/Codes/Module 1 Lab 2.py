# String Operations

# somethig written inside '' or "" is a string

# print ("Nahid Hasan Sagar") # this is a string
# print ("1 + 3 + 5 + 6") # this is also a string

firstName = "Nahid Hasan "
lastName = "Sagar"

fullName = firstName + lastName # this is concatenating

# print (firstName)
# print (lastName)
# print (fullName)

# Indexing 
# print (len(fullName))

# print (fullName[0]) # will show me the first latter

# print (fullName[16]) # will show me the last latter
# print (fullName[-1]) # will also show me the last latter
# print (fullName[13])
# print (fullName[-13]) # negative index will count from the last and start with index no -1

# Slicing 
# print (firstName[:4]) # will give me first 4 characters of the string

# print (fullName[8:13]) # will give me the charecter from index no 8 to 13

# Stride
# print (fullName[::2]) # this will give me every second values
# print (fullName[::3]) # this will give me every third values.

# print (fullName[0:11:2]) # this will give me every second values from 0th index to 11th index

# fullName = fullName + "\nAspiring \t Data Analyst" # \n creates a new line \t adds a tab (4) amount space
# print (fullName)

# fullName = fullName + " here I am showing a back slash \\"
# print (fullName)
# fullName = r"Again showing a \ slash" + firstName
# print (fullName)



# Some String Methods
# firstName = firstName.upper()
# print (firstName) # converts everything into upper case.

# fullName = fullName.replace("Sagar", "")
# print (fullName)

# print (fullName.find("Sag")) # gives me the frist index.
# print (firstName.find("Sagar")) # if couldn't find the answer will be negative 1

#Split the substring into list
name = "Michael Jackson"
split_string = (name.split())
print (split_string)

# Incomplete