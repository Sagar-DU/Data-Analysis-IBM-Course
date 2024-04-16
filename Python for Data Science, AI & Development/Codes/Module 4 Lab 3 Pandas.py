import pandas as pd

#Defining a dictionary 'x'
x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
print (df)
print ("Retriving ID:")
print (df[["ID"]])
print (type(df[["ID"]]))
print("Accessing Multiple Columns:")
print (df[["Department", "Salary", "ID"]])

# iloc access the data with row and column number
print ("iloc output:")
print (df.iloc[0, 0])
print (df.iloc[0, 2])

# loc access the data with name 
print (df.loc[0, "Salary"])

df2 = df
df2 = df2.set_index("Name")
print (df2.head(2))
# shows first 5 elemnts by defult
print (df2.head())
print (df2.loc["Jane", "Salary"])
print (df2.loc["Jane", "Department"])
print (df2.iloc[3,2])

# Slicing 
print (df.iloc[0:2, 0:3])
print (df.loc[0:2, "ID":"Department"])

print (df2.loc["Rose":"Jane", "ID":"Department"])



# Excercise 
# Problem 1: Create a dataframe to display the result as below:
Data = {"Student": ["David", "Samuel", "Terry", "Evan"], "Age": [27, 24, 22, 32], "Country": ["UK", "Canada", "China", "USA"], "Course": ["Python", "Data Structures", "Machine Learning", "Web Development"], "Marks": [85, 72, 89, 75]}

dataFrame = pd.DataFrame(Data)
print (dataFrame)

# Problem 2: Retrieve the Marks column and assign it to a variable b
b = dataFrame[["Marks"]]
print (b)

# Problem 3: Retrieve the Country and Course columns and assign it to a variable c
c = dataFrame[["Country", "Course"]]
print (c)

# To view the column as a series, just use one bracket:
x = dataFrame ["Student"]
print(x)
print(type(x))

# using loc() function, do slicing on old dataframe df to retrieve the Name, ID and department of index column having labels as 2,3
print (df.loc[2:3, "Name":"Department"])

# Completed