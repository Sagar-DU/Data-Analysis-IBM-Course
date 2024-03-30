# First function example

def add (a):
    """
    Add 1 to a
    """
    b = a + 1
    print (a, "if you add one", b)
    return b

# Calling a function
add (5)
add (2)

# Tells you what a function do? But the specification must defined inside the function
help (add)

# Function with multiple variables
def Mult (a, b):
    '''
    Multiplies two number
    '''
    return a * b

print (Mult (3, 2))
print (Mult (3.5, 2))
print (Mult (3, "\nSagar"))
help (Mult)

def squaare (a):
    # Local variable b
    b = 1
    c = a * a + b
    print (a, "if you square + 1,", c)

    return c

squaare (5)

# Initializing Global variable
x = 3

# Making function call and return a y
y = squaare (x)
y

squaare (2)

# Function without retun
def MJ ():
    print ("Michael Jackson")

# Function with none return
def MJr ():
    print ("Michael Jackson with none return")
    return None

MJ ()
MJr ()

# Defining the function combining strings
def con (a, b):
    return a + b

print (con("This", " is cool!"))

# Consider the two lines of code in Block 1 and Block 2: the procedure for each block is identical. The only thing that is different is the variable names and values.
# Block 1
# a and b calculation block1

a1 = 4
b1 = 5
c1 = a1 + b1 + 2 * a1 * b1 - 1
if(c1 < 0):
    c1 = 0 
else:
    c1 = 5
print (c1)

# Block 2
# a and b calculation block2

a2 = 0
b2 = 0
c2 = a2 + b2 + 2 * a2 * b2 - 1
if(c2 < 0):
    c2 = 0 
else:
    c2 = 5
print (c2)

# We can replace the lines of code with a function. A function combines many instructions into a single line of code. Once a function is defined, it can be used repeatedly. You can invoke the same function many times in your program. You can save your function and use it in another program or use someone else’s function. The lines of code in code Block 1 and code Block 2 can be replaced by the following function:

# Making function for the calculation above
def Equation (a, b):
    c = a + b + 2 * a * b - 1
    if (c < 0):
        c = 0
    else:
        c = 5
    
    return c
print (Equation(a1, b1))
print (Equation(a2, b2))

# Using if/else Statements and Loops in 

# If/elase
def type_of_album (artist, album, year_released):
    print (artist, album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"

x = type_of_album ("Michael Jackson", "Thriller", 1980)

print(x)

# Loop
def PrintList (the_list):
    for element in the_list:
        print (element)

PrintList (["1", 1, "The man", "abc"])

# String comparison in Functions
string = "Micheal Jackson"

def chec_string (text):
    if text in string:
        return "String matched"
    else:
        return "String not matched"
    
print (chec_string ("Michael Jackson is the best!"))

# This function receives both strings as its argument and returns 1 if both strings are equal using == operator
def compareStrings (x, y):
    if x == y:
        return 1
    
string1 = "Michael Jackson is the best"
string2 = "Michael Jackson is the best"

check = compareStrings (string1, string2)

if check == 1:
    print ("\n String Matched")
else:
    print ("\n String not Matched")

# Count the Frequency of Words Appearing in a String Using a Dictionary.
def freq (string):
    # step 1: A list variable is declared and initialized to an empty list
    words = []

    # step 2: Break the string into list of words
    words = string.split()
    
    # step 3: Declare a dictonary
    Dict = {}

    # step 4: Use for loop to iterate word into valuess of the dictonary
    for key in words:
        Dict [key] = words.count(key)

    # step 5: Print the dictionary
    print ("The Frequencty of words is:", Dict)

# step 6: Call the function 
freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go")

# Setting default argument values in your custom functions
def isGoodRating(rating=4): 
    if(rating < 7):
        print("this album sucks it's rating is",rating)
        
    else:
        print("this album is good its rating is",rating)

isGoodRating ()
isGoodRating (10)

# Global variables
# Example of global variable

artist = "Michael Jackson"
def printer1(artist):
    internal_var1 = artist
    print(artist, "is an artist")
    
printer1(artist)
# try runningthe following code
#printer1(internal_var1)

artist = "Michael Jackson"

def printer(artist):
    global internal_var 
    internal_var= "Whitney Houston"
    print(artist,"is an artist")

printer(artist) 
printer(internal_var)

# Scope of a Variable
# Example of global variable

myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:", getBandRating("AC/DC"))
print("Deep Purple's rating is:",getBandRating("Deep Purple"))
print("My favourite band is:", myFavouriteBand)

# Deleting the variable "myFavouriteBand" from the previous example to demonstrate an example of a local variable 

del myFavouriteBand

# Example of local variable

def getBandRating(bandname):
    myFavouriteBand = "AC/DC"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is: ", getBandRating("AC/DC"))
print("Deep Purple's rating is: ", getBandRating("Deep Purple"))
# print("My favourite band is", myFavouriteBand)

# Example of global variable and local variable with the same name

myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    myFavouriteBand = "Deep Purple"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:",getBandRating("AC/DC"))
print("Deep Purple's rating is: ",getBandRating("Deep Purple"))
print("My favourite band is:",myFavouriteBand)

# Collections and Functions
def printAll(*args): # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args)) 
    for argument in args:
        print(argument)
#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')

def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')

def addItems(list):
    list.append("Three")
    list.append("Four")

myList = ["One","Two"]

addItems(myList)

print (myList)

# Excercise
# 1. Come up with a function that divides the first input by the second input:
def div (a, b):
    c = a / b
    print (a, "is divede by", b, " = ", c)
    return c

div (6, 3)

# 2. Use the function con for the following question.
# Can the con function we defined before be used to add two integers or strings?

print (con (2,5))
print (con ("2","5"))

# Can the con function we defined before be used to concatenate lists or tuples?
print (con(['a', 1], ['b', 1]))

# 3. Write a function code to find total count of word little in the given string: "Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"**

string = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"

def word_count (string, pasedkey):
    words = []
    words = string.split()

    Dict = {}

    for key in words:
        if key == pasedkey:
            Dict[key] = words.count(key)
    
    print ("Total count of the word", Dict)

word_count (string, "Mary")
word_count (string, "little")
word_count (string, "lamb")