# Range
print (range(5))

# For Loop 
dates = [1982, 1980, 1973]
N = len (dates)

for i in range (N):
    print ("Showing dates with loop:", dates[i])

for i in range (0, 9):
    print ("Another example for loop:", i)
    
for year in dates:
    print ("Using for loop with element:", year)

squares = ["red", "yellow", "green", "purple", "blue"]

for i in range (0, 5):
    print ("Before square ", i, "is", squares[i])
    squares[i] = "white"
    print ("After square ", i, "is", squares[i])

squares = ["red", "yellow", "green", "purple", "blue"]
for i, square in enumerate(squares):
    print (i, square)

# While Loop 
count = 1
while count <= 5:
    print ("Counting with while loop:", count)
    count += 1

# Another example of While Loop 
dates = [1982, 1980, 1973, 2000]
i = 0
year = dates[0]
while (year != 1973):
    i += 1
    year = dates [i]

print ("It took", i, "repetations to get out of loop.")

# Excercises
# 1. Write a for loop the prints out all the element between -5 and 5 using the range function.
for i in range (-4, 5):
    print (i)

# 2. Print the elements of the following list: Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop'] Make sure you follow Python conventions.
Genres = [ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for genre in Genres:
    print ("Here are the Genres:", genre)

# 3. Write a for loop that prints out the following list: squares=['red', 'yellow', 'green', 'purple', 'blue']
squares = ['red', 'yellow', 'green', 'purple', 'blue']
for square in squares:
    print("Here are the color of the squares:", square)

# 4. Write a while loop to display the values of the Rating of an album playlist stored in the list PlayListRatings. If the score is less than 6, exit the loop. The list PlayListRatings is given by: PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
rating = PlayListRatings[i]

while (i < len(PlayListRatings) and rating >= 6):
    print ("Ratings:",rating)
    i += 1
    rating = PlayListRatings[i]

print ("It took", i, "repetations to get out of loop.")

# 5. Write a while loop to copy the strings 'orange' of the list squares to the list new_squares. Stop and exit the loop if the value on the list is not 'orange':
squares = ["orange", "orange", "purple", "blue", "orange"]
new_squares = []
i = 0

while (i < len(squares) and squares[i] == "orange"):
    new_squares.append(squares[i])
    i += 1
print ("It took", i, "repetations to get out of loop.", new_squares)

# 6. Your little brother has just learned multiplication tables in school. Today he has learned tables of 6 and 7. Help him memorise both the tables by printing them using for loop.
for i in range (1, 11):
    print ("Multiplication table of 6:", 6, "*", i, "=", i*6)

for i in range (1, 11):
    print ("Multiplication table of 7:", 7, "*", i, "=", i*7)

# 7. The following is a list of animals in a National Zoo. Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
    # Your brother needs to write an essay on the animals whose names are made of 7 letters. Help him find those animals through a while loop and create a separate list of such animals.
Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
Animals_with_seven_latter_name = []
i = 0
while (i < len (Animals)):
    if (len(Animals[i]) == 7):
        Animals_with_seven_latter_name.append(Animals[i])
    i += 1

print ("Here is the List of animals you neet to write eassy on:", Animals_with_seven_latter_name)

# Completed