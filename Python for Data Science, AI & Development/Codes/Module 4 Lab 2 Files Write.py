# Writing to a file
example2 = "Example2.txt"
with open (example2, "w") as writefile:
    writefile.write("This is line A")

# Now read the file just crated
with open (example2, "r") as testwritefile:
    print ("first output:",testwritefile.read())

with open (example2, "w") as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")

# Now read the file just crated
with open (example2, "r") as testwritefile:
    print ("second output",testwritefile.read())

# sample list 
Lines = ["This is line A \n", "This is line B\n", "This is line C\n"]

# Writing the string in the list to a text file 
with open (example2, "w") as writefile:
    for line in Lines:
        print ("Inside loop output",line)
        writefile.write(line)

with open (example2, "r") as readfromloop:
    print ("Out of the loop output\n", readfromloop.read())

# Note: writing overwites all the existing data 
with open (example2, "w") as writefile:
    writefile.write("Overwritten\n")

with open (example2, "r") as readingoverwrittenfile:
    print (readingoverwrittenfile.read())

# If I want to just add something on a existing file? I need to append
with open(example2, "a") as appendingfile:
    appendingfile.write("This is line A on the overwritten file\n")
    appendingfile.write("This is line B on the overwritten file\n")
    appendingfile.write("This is line C on the overwritten file\n")

with open(example2, "r") as file:
    print (file.read())

# It's a pain in the that every time we need with open to write read. We can do both at the same time with r+, w+, and a+
# Let's try a+
with open (example2, "a+") as testappend:
    # Appending 
    testappend.write("This is line D on the overwritten file\n")
    testappend.write("This is line E on the overwritten file\n")

    # Seek to the beginning of the file before reading again
    testappend.seek(0)

    # Reading 
    print ("Reading with one with:") 
    print(testappend.read())

# with open(example2, "r") as file:
#     print (file.read())
