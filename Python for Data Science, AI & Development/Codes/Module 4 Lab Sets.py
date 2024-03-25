# A set 
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print ("Set doesn't repeart elements:", set1)

# Converting list to set 
album_list = ["Michael Jackson", "Thriller", 1982, "00:42:19", "Pop, Rock, R&B", 46.9, 53, "30-Nov-82", None, 10, 0]

album_set = set (album_list)
print ("This is a set converted from a list:", album_set)

music_genres = set (["pop", "pop", "rock", "folk rock", "hard rock", "soul", "progressive rock", "soft rock", "R&B", "disco"])
print ("This is another set converted from a list:", music_genres)

# Set Operations

# Sample set
A = set(["Thriller", "Back in Black", "AC/DC"])

print ("This my set before any operations:", A)

A.add("NSYNC")
print ("This is my set after adding NSYNC:", A)

A.remove("NSYNC")
print ("This is my set after removing NSYNC:", A)

# Verify if the element is in the set
print ("AC/DC" in A)

# Sets Logic Operations
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

print ("Printing two sets:", album_set1, album_set2)

intersection = album_set1 & album_set2
print ("Intersection of the two sets:", intersection)

print ("Set difference:", album_set1.difference(album_set2))
print ("Set difference:", album_set2.difference(album_set1))

print ("Intersection using method:", album_set1.intersection(album_set2))
print ("Union of the two sets:", album_set1.union(album_set2))

print ("Check subset:", album_set1.issubset(album_set2))
print ("Check subset:", album_set2.issubset(album_set1))

# Check if subset
print ("Check subset:", set({"Back in Black", "AC/DC"}).issubset(album_set1))

# Check if superset
print ("Check superset:", album_set1.issuperset({"Back in Black", "AC/DC"}))

# Excercise

# 1. Convert the list ['rap','house','electronic music', 'rap'] to a set:
print ("This a converted set from the list:", set (['rap','house','electronic music', 'rap']))

# 2. Consider the list A = [1, 2, 2, 1] and set B = set([1, 2, 2, 1]), does sum(A) == sum(B)?
A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])
print ("Sum of all the list elements:", sum(A))
print ("Sum of all the set elements:", sum(B))
print ("They are not the same bro!")

# 3. Create a new set album_set3 that is the union of album_set1 and album_set2:
album_set3 = album_set1.union(album_set2)
print ("Union of Album 1 and 2:", album_set3)

# 4. Find out if album_set1 is a subset of album_set3:
print ("Is Album 1 a subset of Album 3: ", album_set1.issubset(album_set3))

# Completed