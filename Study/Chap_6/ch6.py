import pandas as pd
from textblob import TextBlob

movies = pd.read_csv('.\dataset\\Train.csv')

# print("Number of positive and negative reviews: ", movies.label.value_counts())
# print("Proportion of positive and nagative reviews: ", movies.label.value_counts()/len(movies))
# length_reviews = movies.text.str.len()
# How long is the longest review
# print(min(length_reviews))
# Import the required packages

# text = "That so chill"
# # Create a textblob object
# blob_two_cities = TextBlob(text)
# # Print out the sentiment
# print(blob_two_cities.sentiment)

f = open(".\dataset\\titanic.txt", "r")
titanic = f.read()
# Create a textblob object
blob_titanic = TextBlob(titanic)

# Print out its sentiment
print(blob_titanic.sentiment)