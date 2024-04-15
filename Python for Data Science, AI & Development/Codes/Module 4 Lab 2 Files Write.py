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

# Revisiting a+
with open (example2, "a+") as testingappendplus:
    print ("Initial Location: {}".format(testingappendplus.tell()))

    data = testingappendplus.read()
    if (not data): # means empty string returns flase in python
        print ("Nothing to read!")
    else:
        print (testingappendplus.read())

    testingappendplus.seek(0, 0) # moves 0 bytes from beginning.

    print ("\nNew Location: {}".format(testingappendplus.tell()))

    data = testingappendplus.read()

    if (not data): # means empty string returns flase in python
        print ("Nothing to read!")
    else:
        print (data)
    
    print ("Location after read: {}".format(testingappendplus.tell()))

    with open (example2, "r+") as testwritefile:
        testwritefile.seek(0, 0) #writing at the beginning of the file
        
        testwritefile.write("Line 1" + "\n")
        testwritefile.write("Line 2" + "\n")
        testwritefile.write("Line 3" + "\n")
        testwritefile.write("Line 4" + "\n")
        testwritefile.write("Finished\n")

        testwritefile.truncate() #this will delete everything previously stored on the file
        testwritefile.seek(0,0)
        
        print (testwritefile.read())

# Copying a file 
with open (example2, "r") as readfile:
    with open ("Example3.txt", "w") as writefile:
        for line in readfile:
            writefile.write(line)

with open ("Example3.txt", "r") as readfile:
    print ("This is new file data copied from previous file:")
    print (readfile.read())