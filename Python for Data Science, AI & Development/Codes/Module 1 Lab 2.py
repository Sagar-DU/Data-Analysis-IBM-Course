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
# name = "Michael Jackson"
# split_string = (name.split())
# print (split_string)

import re

# s1 = "Michael Jackson is the best"

# # defining the patteren to search
# pattern = r"Jackson"

# # using the search() function to search for the pattern in the string
# result = re.search (pattern, s1)

# # check if a match was found
# if result:
#     print ("Match found!")
# else:
#     print ("No match!")

# This code will search for phone number
# pattern = r"\d\d\d\d\d\d\d\d\d\d\d" # this line decides how many digits I am looking?
# text = "My phone number is 01521330993"
# match = re.search (pattern, text)

# if match:
#     print ("Phone number found:", match.group())
# else:
#     print ("No mathch!")

# pattern = r"\W"
# text = "Hello, World!"
# matches = re.findall (pattern, text) # match any character that is not a word character (a-z, A-Z, 0-9, or _) & The findall() function finds all occurrences of a specified pattern within a string.

# print ("Matches:", matches)

s2 = "Michael Jackson was a singer and known as the 'King of Pop'"


# # Use the findall() function to find all occurrences of the "as" in the string
# result = re.findall("as", s2)

# # Print out the list of matched words
# print(result)

# uses the split function to split the string by "\s" = space
# split_array = re.split("\s", s2)

# print (split_array)

# pattern = r"king of Pop"
# replacement = "Legend"

# new_string = re.sub (pattern, replacement, s2, flags=re.IGNORECASE)

# print (new_string)

# Complete