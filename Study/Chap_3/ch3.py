from ctypes.wintypes import PINT
from matplotlib import pyplot as plt
import re
from nltk.tokenize import word_tokenize
from collections import Counter
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

counter = Counter(word_tokenize("""The cat is in the box. The cat likes the box. The box is over the cat."""))
# print(counter)
count = counter.most_common(2)
# print(count)

f = open("wiki_article.txt", "r")
article = f.read()

tokens = word_tokenize(article)
lower_tokens = [t.lower() for t in tokens]
# print(lower_tokens)

bow_simple = Counter(lower_tokens)
# print(bow_simple)
# print(bow_simple.most_common(10))

text = """The cat is in the box. The cat likes the box. The box is over the cat."""
tokens = [w for w in word_tokenize(text.lower()) if w.isalpha()]
no_stops = [t for t in tokens if t not in stopwords.words('english')]
# print(Counter(no_stops).most_common(2))



alpha_only = [t for t in lower_tokens if t.isalpha()]
#Remove all stop words : no_stops
no_stops = [t for t in alpha_only if t not in stopwords.words('english')] # ตัดคำที่ไม่ใช้ออก

wordnet_lemmataizer = WordNetLemmatizer()

lemmataized = [wordnet_lemmataizer.lemmatize(t) for t in no_stops]

bow = Counter(lemmataized)
print(bow.most_common(10))
