from randomuser import RandomUser
import pandas as pd

r = RandomUser()

some_list = r.generate_users(10)
print(some_list)

name = r.get_full_name()
for user in some_list:
    print(user.get_full_name(), " ", user.get_email())

# Excercise 
# 1. In this Exercise, generate photos of the random 10 users.
for user in some_list:
    print (user.get_picture())

def get_users():
    users = []

    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
    return pd.DataFrame(users)
print (get_users())
df1 = pd.DataFrame(get_users())

# print (df1)

# Fruityvice API
import requests
import json

data = requests.get("https://fruityvice.com/api/fruit/all")

ressults = json.loads(data.text)
print (pd.DataFrame(ressults))

df2 = pd.json_normalize(ressults)
print (df2)

cherry = df2.loc[df2["name"] == 'Cherry']
(cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])
print (cherry)
print (cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])

# 2. In this Exercise, find out how many calories are contained in a banana.
cal_banana = df2.loc[df2["name"] == "Banana"]
cal_banana.iloc[0]["nutritions.calories"]
print (cal_banana)
print (cal_banana.iloc[0]["nutritions.calories"])

# Joke API
url = "https://official-joke-api.appspot.com/jokes/ten"
data2 = requests.get(url)

ressults2 = json.loads(data2.text)
print (ressults2)

df3 = pd.DataFrame(ressults2)
df3.drop (columns=["type", "id"], inplace=True)
print(df3)