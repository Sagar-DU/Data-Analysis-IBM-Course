# Let's consider a real-life scenario where you are analyzing customer feedback for a product. You have a large data set of customer reviews in the form of strings, and you want to extract useful information from them using the three identified tasks:

# Task 1. String in lowercase: You want to pre-process the customer feedback by converting all the text to lowercase. This step helps standardize the text. Lower casing the text allows you to focus on the content rather than the specific letter casing.

# Task 2. Frequency of all words in a given string: After converting the text to lowercase, you want to determine the frequency of each word in the customer feedback. This information will help you identify which words are used more frequently, indicating the key aspects or topics that customers are mentioning in their reviews. By analyzing the word frequencies, you can gain insights into the most common issues raised by customers.

# Task 3. Frequency of a specific word: In addition to analyzing the overall word frequencies, you want to specifically track the frequency of a particular word that is relevant to your analysis. For example, you might be interested in monitoring how often the word "reliable" appears in customer reviews to gauge customer sentiment about the product's reliability. By focusing on the frequency of a specific word, you can gain a deeper understanding of customer opinions or preferences related to that particular aspect.

# By performing these tasks on the customer feedback dataset, you can gain valuable insights into customer sentiment

# Part A 

# Step 1: Define a string
givenstring = "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

# Step 2: Define the class and its attributes

# Let's create a class called TextAnalyzer to analyze text.
class TextAnalzer(object):
    
    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace(".","").replace("!","").replace(",","")
        # make text lowercase
        formattedText = formattedText.lower()

        self.fmtText = formattedText

# Step 4: Implement a code to count the frequency of all unique words
# class TextAnalzer(object):
    
#     def __init__ (self, text):
#         # removing punctuation
#         formattedText = text.replace(".","").replace("!","").replace(",","")
#         # making text lowercase
#         formattedText = formattedText.lower()

#         self.fmtText = formattedText

#     def freqAll (self):
#         # Splitting the text into words
#         wordList = self.fmtText.split(" ")
#         # Creating a dictionary
#         freqMap = {}
#         for word in set(wordList): # using set to remove duplicates in list
#             freqMap[word] = wordList.count(word)

#         return freqMap
    
# Step 5: Implement a code to count the frequency of a specific word
class TextAnalzer(object):
    
    def __init__ (self, text):
        # removing punctuation
        formattedText = text.replace(".","").replace("!","").replace(",","")
        # making text lowercase
        formattedText = formattedText.lower()

        self.fmtText = formattedText

    def freqAll (self):
        # Splitting the text into words
        wordList = self.fmtText.split(" ")
        # Creating a dictionary
        freqMap = {}
        for word in set(wordList): # using set to remove duplicates in list
            freqMap[word] = wordList.count(word)

        return freqMap
    def freqOf (self, word):
        # getting the frequency map
        freqDict = self.freqAll()

        if word in freqDict:
            return freqDict[word]
        else:
            return 0
        
# Part B 

# Step 1: Creating an instance of TextAnalyzer class
analyzed = TextAnalzer(givenstring)

# Step 2: Calling the function that converts the data into lowercase
print ("Formatted Text", analyzed.fmtText)

# Step 3: Call the function that counts the frequency of all unique words from the data
freqMap = analyzed.freqAll()
print(freqMap)

# Step 4: Call the function that counts the frequency of a specific word
# Here, you will call the function that counts the frequency of the word "lorem".

# Print the output.**
word = "lorem"
frequency = analyzed.freqOf(word)
print("Frequecny of ", word, ":", frequency)

# Completed