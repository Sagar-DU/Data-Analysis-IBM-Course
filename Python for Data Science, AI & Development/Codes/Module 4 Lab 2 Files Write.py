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

# Excercise
# 1. Your local university's Raptors fan club maintains a register of its active members on a .txt document. Every month they update the file by removing the members who are not active. You have been tasked with automating this with your Python skills.
# Given the file currentMem, Remove each member with a 'no' in their Active column. Keep track of each of the removed members and append them to the exMem file. Make sure that the format of the original files in preserved. (Hint: Do this by reading/writing whole lines and ensuring the header remains )
# Run the code block below prior to starting the exercise. The skeleton code has been provided for you. Edit only the cleanFiles function.
from random import randint as rnd
memReg = "members.txt"
exReg = "inactive.txt"
fee = ("yes", "no")

def genFiles (current, old):
    with open (current, "w+") as writefile:
        writefile.write("Membership No Data Joined Active \n")
        data = "{:^13} {:<11} {:<6} \n"

        for rowno in range(20):
            date = str (rnd (2015, 2020)) + "-" + str (rnd (1, 12)) + "-" + str (rnd(1, 25))
            writefile.write(data.format(rnd(10000, 99999), date, fee[rnd(0,1)]))

    with open (old, "w+") as writefile:
        writefile.write ("Membership No Date Joined Active \n")
        data = "{:^13} {:<11} {:<6} \n"

        for rowno in range (3):
            date = str (rnd (2015, 2020)) + "-" + str (rnd (1, 12)) + "-" + str (rnd(1, 25))
            writefile.write(data.format(rnd(10000, 99999), date, fee[1]))

genFiles (memReg, exReg)