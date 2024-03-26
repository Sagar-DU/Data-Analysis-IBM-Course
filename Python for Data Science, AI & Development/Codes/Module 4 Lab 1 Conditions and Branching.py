# Comparison
a = 5
print (a == 6)

i = 6
print (i > 5)
i = 2
print (i > 5)

print (i != 6)
i = 6
print (i != 6)

# comparing strings
print ("ACDC" == "Michael Jackson")
print ("ACDC" != "Michael Jackson")

print ("B" > "A")

# When there are multiple letters, the first letter takes precedence in ordering:
print ("BA" > "AB")

# If statement example
age = 19
#expression that can be true or false
# if age > 18:
#     #within an indent, we have the expression that is run if the condition is true
#     print("you can enter" )

# #The statements after the if statement will run regardless if the condition is true or false 
# print("move on")

age = 18
# if age > 18:
#     #within an indent, we have the expression that is run if the condition is true
#     print("you can enter" )

# #The statements after the if statement will run regardless if the condition is true or false 
# print("move on")

# Elif statment example
if age > 18:
    print("you can enter" )
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf" )
    
print("move on")

# Condition statement example
album_year = 1983

if album_year > 1980:
    print("Album year is greater than 1980")
    
print('do something..')

album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")
else:
    print("less than 1980")

# Logical Operators and or not 
album_year = 1980

if(album_year > 1979) and (album_year < 1990):
    print ("Album year was in between 1980 and 1989")
    
print("")
print("Do Stuff..")

album_year = 1990

if(album_year < 1980) or (album_year > 1989):
    print ("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")

album_year = 1983

if not (album_year == 1984):
    print ("Album year is not 1984")

# Exercise

# 1. Write an if statement to determine if an album had a rating greater than 8. Test it using the rating for the album “Back in Black” that had a rating of 8.5. If the statement is true print "This album is Amazing!"

rating = 8.5

if rating > 8:
    print ("Back in Black is Amazing!")

# 2. Write an if-else statement that performs the following. If the rating is larger then eight print “this album is amazing”. If the rating is less than or equal to 8 print “this album is ok”.
rating = 7    

if rating > 8:
    print ("This Album is Amazing!")

elif rating <= 8:
    print ("This Album is ok.")

# 3. Write an if statement to determine if an album came out before 1980 or in the years: 1991 or 1993. If the condition is true print out the year the album came out.
album_year = 1979

if album_year == 1991 or album_year == 1983:
    print ("This album came either in", album_year)
else:
    print ("This album did not come either in 1983 or 1991")

album_year = 1991
if album_year == 1991 or album_year == 1983:
    print ("This album came either in", album_year)
else:
    print ("This album did not come either in 1983 or 1991")

