import requests
import pandas as pd

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv"
filename = "TopSellingAlbums.csv"

# Download the CSV file
'''
response = requests.get(url)
if response.status_code == 200:
    with open(filename, "wb") as f:
        f.write(response.content)
'''

# Read the CSV file into a DataFrame
df = pd.read_csv(filename)

# Now you can work with the DataFrame as usual
print ("CSV DATA:")
print(df.head())

# Define the URL of the Excel file
xlsx_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/jupyterlite/files/Module%205/data/TopSellingAlbums.xlsx'

# Define a function to download files
'''
def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
    else:
        print("Failed to download the file.")

# Download the Excel file
download(xlsx_path, "TopSellingAlbums.xlsx")
'''

# Read the Excel file into a DataFrame
df = pd.read_excel("TopSellingAlbums.xlsx")

# Print the first five rows of the DataFrame
print ("Excel DATA:")
print(df.head())

# Accessing Column, Length
x = df[["Length"]]
print(x)
x = df[["Artist"]]
print(x)
print(type(x))

y = df[["Artist", "Length", "Genre"]]
print(y)

print(df)
print (df.iloc[0,0])
print (df.iloc[1,0])
print (df.iloc[0,2])
print (df.iloc[1,2])
print(df)
print ("Loc output")
print (df.loc[1, "Artist"])
print (df.loc[0, "Released"])
print (df.loc[1, "Released"])

print ("Slicing")
print (df.iloc[0:2, 0:3])
print (df.loc[0:2, 'Artist':'Released'])

# Exercise 
# 1. Use a variable q to store the column Rating as a dataframe
q = df[["Rating"]]
print (q)

# 2. Assign the variable q to the dataframe that is made up of the column Released and Artist:
q = df[["Released", "Artist"]]
print (q)

# 3. Access the 2nd row and the 3rd column of df:
print (df)
access = df.iloc[1, 2]
print (access)

# 4. Use the following list to convert the dataframe index df to characters and assign it to df_new; find the element corresponding to the row index a and column 'Artist'. Then select the rows a through d for the column 'Artist'
new_index=['a','b','c','d','e','f','g','h']

df_new = df
df_new.index = new_index
print (df_new.loc["a":"h", "Artist"])

# Completed