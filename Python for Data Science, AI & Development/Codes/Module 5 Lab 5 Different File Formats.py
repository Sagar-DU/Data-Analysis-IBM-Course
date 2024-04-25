import pandas as pd
import requests

# CSV 

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv"

# Download Function 

def download (url, filename):
    response = requests.get (url)
    if response.status_code == 200:
        with open (filename, "wb") as f:
            f.write(response.content)

# download(filename, "addresses.csv")
df = pd.read_csv("addresses.csv", header=None)
print (df)

df.columns =['First Name', 'Last Name', 'Location ', 'City','State','Area Code']
print (df)
print (df["First Name"])

df = df[['First Name', 'Last Name', 'Location ', 'City','State','Area Code']]
print (df)

print ("loc output:")
print (df.loc[0])
print (df.loc[[0, 1, 2,], "First Name"])

print ("iloc output:")
print (df.iloc[[0, 1, 2,], 0])

import numpy as np
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns = ["a", "b", "c"])
print (df)

print ("Transformatin:")
df = df.transform(func = lambda x : x + 10)
print(df)

result = df.transform (func = ["sqrt"])
print (result)

# JSON
import json

person = {
    "first_name" : "Mark",
    "last_name" : "abc",
    "age" : 27,
    "address" : {
        "streetAddress" : "21 2nd Street",
        "city" : "New York",
        "state" : "NY",
        "postCode" : "10021-3100"
    }
}

with open ("person.json", "w") as f: # writing JSON object
    json.dump(person, f)

# Seralizing json 
json_object = json.dumps(person, indent=4)

# Writing to sample json 
with open ("sample.json", "w") as outfile:
    outfile.write(json_object)

print ("\t JSON Object")
print (json_object)

# Opening JSON file 
with open ("sample.json", "r") as openfile:
    # Reading from json file
    json_object = json.load(openfile)

print ("Reading from JSON Object:")
print (json_object)
print (type(json_object))

# XLSX 
import urllib.request

urllib.request.urlretrieve("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx", "sample.xlsx")

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx"

# Downloading 
# download(filename, "file_example_XLSX_10.xlsx")

import xml.etree.ElementTree as ET

# Creating the file stracture
employee = ET.Element("employee")
details = ET.SubElement (employee, "details")
first = ET.SubElement (details, "firstname")
second = ET.SubElement (details, "lastname")
third = ET.SubElement (details, "age")
first.text = "Shiv"
second.text = "Mishra"
third.text = "23"

# Creating a new XML file with results
mydata1 = ET.ElementTree(employee)
# myfile = open("items2.xml", "wb")
# myfile.write(mydata)
with open ("new_sample.xml", "wb") as files:
    mydata1.write(files)

# Reading with xml.etree.ElementTree 
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Sample-employee-XML-file.xml"

# Downloading 
# download (filename, "Sample-employee-XML=file.xml")

tree = ET.parse ("Sample-employee-XML=file.xml")

root = tree.getroot()
columns = ["firstname", "lastname", "title", "division", "building", "room"]
dataframe = pd.DataFrame(columns = columns)

for node in root:

    firstname = node.find("firstname").text

    lastname = node.find("lastname").text

    title = node.find("title").text

    division = node.find("division").text

    building = node.find("building").text

    room = node.find("room").text

    dataframe = pd.concat([dataframe, pd.Series([firstname, lastname, title, division, building, room], index=columns)], ignore_index=True)

print (dataframe)

# Herein xpath we mention the set of xml nodes to be considered for migrating  to the dataframe which in this case is details node under employees.
df=pd.read_xml("Sample-employee-XML=file.xml", xpath="/employees/details") 

print (pd)

# Save Data 
dataframe.to_csv("employee.csv", index=False)

# Binary File Format
from PIL import Image
urllib.request.urlretrieve("https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg", "dog.jpg")

filename = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg"

# Downloading 
# download (filename, "./dog.jpg")

# Read Image 
img = Image.open ("./dog.jpg", "r")

# Output Image 
# img.show()
# Cool!!

# Data Analysis
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"

# Downloading 
# download (filename, "diabetes.csv")

df = pd.read_csv ("diabetes.csv")

# Showing first 5 rows using dataframe head() method
print ("The first 5 rows of the dataFrame:")
print (df.head())
print (df.shape)

# Statistical Overview of dataset
print (df.info())
print (df.describe())

# Identify and handle missing values
missing_data = df.isnull()
print (missing_data.head())

# Count missing values in each column
for column in missing_data.columns.values.tolist():
    print (column)
    print (missing_data[column].value_counts())
    print (" ")

# Visualization
import matplotlib.pyplot as plt

labels = "Not diabetic", "Diabetic"
plt.pie (df["Outcome"].value_counts(),labels=labels, autopct = "%0.02f%%")
plt.legend()
plt.show()