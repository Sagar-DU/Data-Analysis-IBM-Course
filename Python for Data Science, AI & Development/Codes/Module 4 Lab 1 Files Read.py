# # Uncomment these if working locally, else let the following code cell run.

# import urllib.request
# url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
# filename = 'Example1.txt'
# urllib.request.urlretrieve(url, filename)

# # Download Example file
# # !wget Example1.txt https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt

print ("Done!")

# # Reading the Example1.txt file
example1 = "Example1.txt" # case doesn't matter
# file1 = open(example1, "r")

# print(file1.name)
# print(file1.mode)

# FileContent = file1.read()
# print (FileContent)

# file1.close()

# Better Way to Open a File (no file closing needed)

# Opeing file using with 
with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)

print (file1.closed)
print (FileContent)

# Reading the first four characters
with open(example1, "r") as file1:
    print (file1.read(4))
    print (file1.read(4))
    print (file1.read(7))
    print (file1.read(15))
print("New way")
with open(example1, "r") as file1:
    print (file1.read(16))
    print (file1.read(5))
    print (file1.read(9))

# Reading one line at a time 
with open(example1, "r") as file1:
    print ("first line: " + file1.readline())

# Readline does not read past one line 
with open(example1, "r") as file1:
    print (file1.readline(20))
    print (file1.readline(20))

# Looping through each line 
with open(example1, "r") as file1:
    count = 0
    for line in file1:
        count +=1
        print("Iteration", str(count), ":", line)

# Using readlines to save the text file to a list
with open (example1, "r") as file1:
    FileasList = file1.readlines()

print(FileasList[0])
print(FileasList[1])
print(FileasList[2])