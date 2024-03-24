# Create a Dictionary and access the elements
Dict = {"key1": 1, "key2": "2", "key3":[3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
print("This is a dictonary:", Dict)

# accessing the value by key
print ("The value of the first key:", Dict["key1"])
print ("This key is a tuple:", Dict[(0, 1)])
# Keys are immutable

release_year_dict = {"Thriller": "1982", "Back in Black": "1980", "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", "Bat Out of Hell": "1977", "Their Greatest Hits (1971 - 1975)": "1976", "Saturday Night Fever": "1977", "Rumours": "1977"}

print ("Release Year of Some Movies:", release_year_dict)
print ("Thriller Movie Release Year:", release_year_dict["Thriller"])
print ("Name (Key) of the Movies:", release_year_dict.keys())
print ("Values of the dictionary:", release_year_dict.values())

# appending a dictionary data
release_year_dict["Gurdian"] = "2007"
print("Updated Movie dictornary:", release_year_dict)

# deleting a dictionary data 
del (release_year_dict["Thriller"])
print ("New Dictonary after delete:", release_year_dict)

# verifying the key is in the dictionary
print ("The Bodyguard" in release_year_dict)

# Excercis
soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}

# 1. In the dictionary soundtrack_dic what are the keys?
print ("Keys of the Soundtrack Dictionary:", soundtrack_dic.keys())

# 2. In the dictionary soundtrack_dic what are the values?
print ("The values of the Soundtrack Dictionary:", soundtrack_dic.values())

# 3. The Albums Back in Black, The Bodyguard and Thriller have the following music recording sales in millions 50, 50 and 65 respectively:
# a) Create a dictionary album_sales_dict where the keys are the album name and the sales in millions are the values.
album_sales_dict = {"Back in Black": "50 millions", "The Bodyguard": "50 millions", "Thriller": "65 millions"}
print("Album Sale Dictionary:", album_sales_dict)

# b) Use the dictionary to find the total sales of Thriller:
print ("The total sales of Thriller:", album_sales_dict["Thriller"])

# c) Find the names of the albums from the dictionary using the method keys():
print ("Name of the Album:", album_sales_dict.keys())

# d) Find the values of the recording sales from the dictionary using the method values:
print ("Sales of the Album:", album_sales_dict.values())

# 4. First you need to create an empty dictionary, where you will be storing the product details.
inventory = {}

# 5. Task-2 Store the first product details in variable
ProductNo1 = "Mobile Phone"
ProductNo1_Quantity = 5
ProductNo1_Price = 20000
ProductNo1_Release_Year = 2020

# 6. Add the details in inventory
inventory["ProductNo1"] = ProductNo1
inventory["ProductNo1_Quantity"] = ProductNo1_Quantity
inventory["ProductNo1_Price"] = ProductNo1_Price
inventory["ProductNo1_Release_Year"] = ProductNo1_Release_Year

# 7. Store the second product details in a variable.
ProductNo2 = "Laptop"
ProductNo2_Quantity = 10
ProductNo2_Price = 50000
ProductNo2_Release_Year = 2023

# 8. Add the item detail into the inventory.
inventory["ProductNo2"] = ProductNo2
inventory["ProductNo2_Quantity"] = ProductNo2_Quantity
inventory["ProductNo2_Price"] = ProductNo2_Price
inventory["ProductNo2_Release_Year"] = ProductNo2_Release_Year

# 9. Display the Products present in the inventory
print (inventory)

# 10. Check if ProductNo1_releaseYear and ProductNo2_releaseYear is in the inventory
print ("ProductNo1_Release_Year" in inventory)
print ("ProductNo2_Release_Year" in inventory)

# 11. Delete release year of both the products from the inventory
del (inventory["ProductNo1_Release_Year"])
del (inventory["ProductNo2_Release_Year"])
print ("ProductNo1_Release_Year" in inventory)
print ("ProductNo2_Release_Year" in inventory)

# Completed